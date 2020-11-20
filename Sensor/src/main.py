from time import sleep
import upip
import ujson
import machine
import ubinascii
import network
import mqttrobust
import mqttsimple
import BME280

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
client_id = ubinascii.hexlify(machine.unique_id())

# Config start
server_ip = "REMOVED"
SSiD = "REMOVED"
password = "REMOVED"
device_id = "REMOVED"
# Config end

def connect_to_internet():
    global SSiD, password, sta_if
    sta_if.active(True)
    sta_if.connect(SSiD, password)
    while not sta_if.isconnected():
        print("Not connected. Retrying...")
        sleep(1)
    print("Connected!")


def transmit_measurements(delay=5):
    global sta_if
    client = mqttrobust.MQTTClient(client_id=client_id, user="REMOVED", password="REMOVED", server=server_ip)

    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=10000)
    bme = BME280.BME280(i2c=i2c)

    while sta_if.isconnected():
        try:
            msg = ujson.dumps({
                "temperature": bme.temperature,
                "humidity": bme.humidity,
                "air_pressure": bme.pressure
            })
            print(msg)
            try:
                client.connect()
                client.publish(topic="sensors/" + str(device_id) + "/measurements", msg=msg)
                client.disconnect()
            except OSError:
                print("Connecting to MQTT server failed.")
            sleep(delay)
        except mqttsimple.MQTTException:
            break
            print("Machine broke")


connect_to_internet()
transmit_measurements(1)
machine.reset()
