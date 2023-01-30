from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from datetime import date
from datetime import datetime
import time

app = Flask(__name__)

# Global vars to hold date ranges
today = date.today().strftime("%Y-%m-%d")
start = f"{today}T00:00:00.000"
end = f"{today}T23:59:59.000"

@app.route('/')
def hello_world():  # put application's code here
    return render_template('main.html')

@app.route('/get_time')
def get_time():
    """
    Used to initialise the RPi Pico datetime as it as no onboard clock reference
    :return:
    """
    now = datetime.today().strftime("%Y,%m,%d,%w,%H,%M,%S,0")
    print(now)
    return now

@app.route('/graph', methods=['GET', 'POST'])
def get_graph():
    name = "Graph Page!"
    try:
        daterange=request.args.to_dict()
        print(request.args.to_dict())
        global start
        start=daterange['start']
        global end
        end=daterange['end']
        print(f"start = {start}")
        print(f"end = {end}")
    except:
        pass

    return render_template('graph.html')


@app.route('/level', methods=['GET', 'POST'])
def get_level():
    """
    http://localhost:3000/level?start=2023-01-29T00:00:00&end=2023-01-29T10:00:00
    :param range:
    :return:
    """
    name = "Tank Level Page!"
    print(f"request.args = {request.args}")
    try:
        daterange=request.args.to_dict()
        print(request.args.to_dict())
        global start
        start=daterange['start']
        global end
        end=daterange['end']
        print(f"start = {start}")
        print(f"end = {end}")
    except:
        pass
    return render_template('level.html')

@app.route('/table', methods=['POST', 'GET'])
def get_table():
    try:
        daterange=request.args.to_dict()
        print(request.args.to_dict())
        global start
        start=daterange['start']
        global end
        end=daterange['end']
        print(f"start = {start}")
        print(f"end = {end}")
    except:
        pass

    return render_template('table.html')

@app.route('/add', methods=['POST', 'GET'])
def add_data():
    # mongo_client = MongoClient("mongodb://localhost:27017/hotwater")
    mongo_client = MongoClient("mongodb://hotuser:password1@localhost:27017/hotwater")
    database = mongo_client.hotwater
    temps = database.temp_data
    print(request.json)
    temps.insert_one(request.json)
    return "."

@app.route('/data', methods=['GET'])
def get_data():
    # mongo_client = MongoClient("mongodb://localhost:27017/hotwater")
    mongo_client = MongoClient("mongodb://hotuser:password1@localhost:27017/hotwater")
    database = mongo_client["hotwater"]
    temps = database["temp_data"]

    print(f"Getting data with range: {start} to {end}")
    d = temps.find({'time':{'$gte': start,'$lt': end}}).sort('time')
    print(d)
    data = []
    for _d in d:
        for _e in _d['data']:
         data.append(_e)
    return {'data' : data}

@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    mongo_client = MongoClient("mongodb://hotuser:password1@localhost:27017/hotwater")
    database = mongo_client["hotwater"]
    temps = database["temp_data"]

    print(f"Getting data with range: {start} to {end}")
    d = temps.find({'time':{'$gte': start,'$lt': end}}).sort('time')
    print(d)
    inner = {}
    data = []
    for _d in d:
        data.append({'time': _d['time']})
        print(inner)
        for _e in _d['data']:
            print(_e)
            data.append(_e)
        # data.append(inner)

    print({'data' : data})
    return {'data' : data}

@app.route('/threshold', methods=['POST', 'GET'])
def threshold():
    """
    Sets the threshold at which the water is detected as hot.
    :return:
    """
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
