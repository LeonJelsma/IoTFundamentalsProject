import asyncio
import datetime
import re
import time
import json
import threading
from collections import deque
from time import sleep
import azure.iot.device as device

from azure.iot.device import IoTHubDeviceClient
from paho.mqtt.client import MQTTMessage

import db_access


class IoTMessenger(threading.Thread):
    def __init__(self, msg_stack: deque):
        self.conn = db_access.create_connection()
        self.msg_stack = msg_stack
        conn_str = "REMOVED"

        self.device_client: IoTHubDeviceClient = IoTHubDeviceClient.create_from_connection_string(conn_str)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            asyncio.run(self.check_messages())
            asyncio.run(self.process_stored_measurements())
            sleep(1)

    async def handle_measurement(self, measurement, store_on_fail=False):
        try:
            self.device_client.connect()
            self.device_client.send_message(json.dumps(measurement))
            self.device_client.disconnect()
            return True
        except (device.exceptions.ClientError,
                device.exceptions.ConnectionDroppedError,
                device.exceptions.ConnectionFailedError):
            if store_on_fail:
                print("Storing failed message")
                self.store_measurement(measurement)
            return False

    async def check_messages(self):
        if len(self.msg_stack) > 0:
            msg: MQTTMessage = self.msg_stack.pop()
            measurement = self.parse_message(msg)
            print(json.dumps(measurement))
            await self.handle_measurement(measurement, True)

    @staticmethod
    def parse_message(message):
        payload = message.payload.decode("utf-8")
        measurement = json.loads(payload)
        measurement["timestamp"] = datetime.datetime.utcfromtimestamp(
            time.mktime(datetime.datetime.now().timetuple())).strftime('%Y-%m-%d %H:%M:%S')
        measurement["deviceId"] = message.topic.replace("sensors/", "").replace("/measurements", "")
        return measurement

    @staticmethod
    def store_measurement(measurement):
        conn = db_access.create_connection()
        db_access.add_measurement(conn, measurement)

    @staticmethod
    def store_measurement(measurement):
        conn = db_access.create_connection()
        db_access.failed_measurements_exist(conn)
        db_access.add_measurement(conn, measurement)

    async def process_stored_measurements(self):
        conn = db_access.create_connection()
        if db_access.failed_measurements_exist(conn):
            measurements = db_access.get_measurements(conn)
            for measurement in measurements:
                id = measurement.pop("id", None)
                success = await self.handle_measurement(measurement, False)
                if success and id is not None:
                    db_access.delete_measurement(conn, id)
        else:
            return

