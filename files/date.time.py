from flask import Flask
from datetime import datetime
app = Flask(__name__)
now = datetime.now()


@app.route('/time')
def datetime():
	data = []
	data.append({"year":now.year, "month":now.month, "day":now.day, "hour":now.hour, "minutes":now.minute, "seconds": now.second})
	return {"data":data}

if __name__ == '__main__':
    app.run()   