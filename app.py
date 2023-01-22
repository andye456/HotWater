from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('main.html')


@app.route('/graph', methods=['GET', 'POST'])
def get_graph():
    name = "Graph Page!"
    return render_template('graph.html')


@app.route('/level', methods=['GET', 'POST'])
def get_level():
    name = "Tank Level Page!"
    return render_template('level.html')


@app.route('/add', methods=['POST', 'GET'])
def add_data():
    # mongo_client = MongoClient("mongodb://localhost:27017/hotwater")
    mongo_client = MongoClient("mongodb://hotuser:password1@localhost:27017/hotwater")
    database = mongo_client.hotwater
    temps = database.temp_data
    temps.insert_one(request.json)
    return "."

@app.route('/data', methods=['GET'])
def get_data():
    # mongo_client = MongoClient("mongodb://localhost:27017/hotwater")
    mongo_client = MongoClient("mongodb://hotuser:password1@localhost:27017/hotwater")
    database = mongo_client["hotwater"]
    temps = database["temp_data"]

    today = date.today().strftime("%Y-%m-%d")

    start = f"{today}T00:00:00.000"
    end = f"{today}T23:59:59.000"

    # data = {'data': temps.find_one()['data']}
    d = temps.find({'time':{'$gte': start,'$lt': end}}).sort('time')
    print(d)
    data = []
    for _d in d:
        for _e in _d['data']:
         data.append(_e)
    return {'data' : data}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
