#!/usr/bin/python

import string
import sqlite3 as lite
import sys
from random import randint


def getTemp():
	tempFile = open('/sys/bus/w1/devices/28-00000529fbad/w1_slave', 'r')
	contents = tempFile.read()
	contentsList = string.split(contents)
	temp = string.split(contentsList[-1])
	temp = str(''.join(temp)).replace('t=', '')
	tempFile.close()
	return temp

def insertTemp():
	temp = getTemp()
	with connection:
		cursor = connection.cursor();
		cursor.execute('INSERT INTO temp(temp_instance) VALUES(?)', (temp,))
		connection.commit()
		print temp

if __name__ == '__main__':
	connection = lite.connect('weather.db')
	insertTemp()