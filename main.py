import json

import paho.mqtt.client as mqtt
from readPerformRobotAction import displayScreen


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to controller")
        client.subscribe("RCat/Pepa")
    else:
        print("Unsuccessful connection, try again later")


def on_message(client, userdata, msg):
    message = str(msg.payload)[2:-1]
    displayScreen(message)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
