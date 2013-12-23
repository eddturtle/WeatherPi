#!/usr/bin/python

import time
import datetime as dt
import sqlite3 as lite
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def connectDB():
	connection = lite.connect('weather.db')
	connection.row_factory = dictFactory
	return connection

def dictFactory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getData(begin, end):
	connection = connectDB()
	with connection:
		cursor = connection.cursor()
		query = 'SELECT temp_instance, temp_date \
				 FROM temp \
				 WHERE temp_date > ? \
				 AND temp_date < ? \
				 ORDER BY temp_date DESC'
		cursor.execute(query, (begin, end))
		data = cursor.fetchall()
		return data

def getAverage():
	connection: connectDB()
	with connection:
		cursor = connection.cursor()
		query = 'SELECT AVG(temp_instance) \
				 FROM temp'
		cursor.execute(query,)
		data = cursor.fetchall()
		return data


@app.route('/api/v1/<int:begin>/<int:end>', methods = ['GET'])
def getTemperatures(begin, end):
	if end == 0:
		end = time.time()
	begin = dt.datetime.fromtimestamp(begin)
	end = dt.datetime.fromtimestamp(end)
	return jsonify({ "average": getAverage(), "instances": getData(begin, end) })

@app.route('/')
def home():
	return render_template('index.htm')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = False)

