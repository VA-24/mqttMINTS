import csv
from getmac import get_mac_address as gma
import random
import time

macaddr = gma()
mac_csv = macaddr.replace(":", "")
weathersensor_id = "BME20"
rainsensor_id = "GCCG41"

fieldnames = ["dateTime", "Temperature", "Pressure", "Humidity", "Altitude"]

with open(f'{mac_csv}_{weathersensor_id}.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()