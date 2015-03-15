import serial
import csv

data = serial.Serial("COM8", 9600)

path = "data.csv"

b = open(path, "wb")
a = csv.writer(b)
a.writerows(data)
b.close()
