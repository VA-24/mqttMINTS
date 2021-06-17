import csv
import random
import time

fieldnames = ["x_value", "speed_data"]


with open('speed.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()