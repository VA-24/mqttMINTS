import paho.mqtt.client as mqtt
from getmac import get_mac_address as gma
import time
import csv
import datetime
import json
import collections

macaddr = gma()
mac_name = macaddr.replace(":", "")
weathersensor_id = "BME20"
rainsensor_id = "GCCG41"

def on_connect(client, userdata, flags, rc):
    client.subscribe(f"{mac_name}/{rainsensor_id}")
    client.subscribe(f"{mac_name}/{weathersensor_id}")


def on_message(client, userdata, message):
    [node_id, sensor_id] = message.topic.split("/")
    print(sensor_id)
    decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
    sensorDict = decoder.decode(message.payload.decode("utf-8","ignore"))
    print(str(sensorDict))
    with open(f"{mac_name}_{sensor_id}.json", "w") as fp:
        json.dump(message.payload.decode("utf-8"), fp)
    data = []
    for key, value in sensorDict.items():
        data.append(value)
    with open(f"{mac_name}_{sensor_id}.csv", "a") as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(data)
    print("-"*20)


#random broker hosting

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Database")
client.connect(mqttBroker)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()