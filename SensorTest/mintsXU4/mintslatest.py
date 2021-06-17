import json
import csv
from getmac import get_mac_address as gma
import time

macaddr = gma()
mac_topicname = macaddr.replace(":", "")
mac_name = macaddr.replace(":", "")
weathersensor_id = "BME20"
rainsensor_id = "GCCG41"

def readJSONLatestAllMQTT():
    with open(f"{mac_topicname}_{weathersensor_id}.json") as myfile:
        dataRead = json.load(myfile)
    time.sleep(0.01)
    return dataRead, True