from flask import Flask
from flask import jsonify
import csv


app = Flask(__name__)

filename = 'iris.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)

print(x)

@app.route('/')
def readtexto():
	  
	return jsonify(x)

if __name__ == '__main__':
    app.run() 