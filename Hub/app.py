import asyncio
import paho.mqtt.client as mqtt

import db_access
from IoTMessenger import IoTMessenger

msg_stack = []
db_access.init_database()


def on_message(_client, userdata, msg):
    global msg_stack
    msg_stack.append(msg)
    #print(msg.topic+" "+str(msg.payload))


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


async def main():
    mqttClient = mqtt.Client()
    mqttClient.username_pw_set(username="REMOVED", password="REMOVED")
    mqttClient.on_message = on_message
    mqttClient.on_connect = on_connect
    mqttClient.connect(host="REMOVED", port=REMOVED)
    mqttClient.subscribe("sensors/+/measurements")
    mqttClient.loop_forever()

if __name__ == "__main__":
    messenger = IoTMessenger(msg_stack)
    messenger.start()
    asyncio.run(main())
