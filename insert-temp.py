#!/usr/bin/python

import sqlite3 as lite
import sys
from random import randint


def getTemp():
	temp = randint(10000, 30000)
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
