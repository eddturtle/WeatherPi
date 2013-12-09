#!/usr/bin/python

import sqlite3 as lite
import sys
from random import randint


def getTemp():
	tempFile = open('/sys/bus/w1/devices/28-00000529fbad/w1_slave', 'r')
	contents = tempFile
    tempFile.seek(0)
    contentsList = string.split(contents)
    temp = contentsList[-1]
    tempFile.close()
	return temp

def insertTemp():
	temp = getTemp()
	with connection:
		cursor = connection.cursor();
		cursor.execute('INSERT INTO temp(temp_instance) VALUES(?)', (temp,))
		connection.commit()

def getData():
	with connection:
		cursor = connection.cursor()
		cursor.execute('SELECT * FROM temp')
		data = cursor.fetchall()
		print data


if __name__ == '__main__':
	connection = lite.connect('weather.db')
	insertTemp()
	getData()
