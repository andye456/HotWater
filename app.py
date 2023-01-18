from flask import Flask, request, render_template

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
@app.route('/data', methods=['GET'])
def get_data():
    data = [
            {"id":"t1", "time": "2023-01-15T10:50:00.000", "temp": 20.432},
            {"id":"t2", "time": "2023-01-15T10:50:00.000", "temp": 21.672},
            {"id":"t3", "time": "2023-01-15T10:50:00.000", "temp": 25.245},
            {"id":"t4", "time": "2023-01-15T10:50:00.000", "temp": 60.223},
            {"id":"t5", "time": "2023-01-15T10:50:00.000", "temp": 75.232},
            {"id":"t6", "time": "2023-01-15T10:50:00.000", "temp": 75.232},
            {"id":"t7", "time": "2023-01-15T10:50:00.000", "temp": 75.232},
            {"id":"t8", "time": "2023-01-15T10:50:00.000", "temp": 75.232},
            {"id":"t9", "time": "2023-01-15T10:50:00.000", "temp": 75.232},
            {"id":"t10","time": "2023-01-15T10:50:00.000", "temp": 75.232},

            {"id":"t1", "time": "2023-01-15T10:55:00.000", "temp": 19.432},
            {"id":"t2", "time": "2023-01-15T10:55:00.000", "temp": 20.672},
            {"id":"t3", "time": "2023-01-15T10:55:00.000", "temp": 23.245},
            {"id":"t4", "time": "2023-01-15T10:55:00.000", "temp": 40.223},
            {"id":"t5", "time": "2023-01-15T10:55:00.000", "temp": 65.232},
            {"id":"t6", "time": "2023-01-15T10:55:00.000", "temp": 73.232},
            {"id":"t7", "time": "2023-01-15T10:55:00.000", "temp": 74.987},
            {"id":"t8", "time": "2023-01-15T10:55:00.000", "temp": 74.232},
            {"id":"t9", "time": "2023-01-15T10:55:00.000", "temp": 76.232},
            {"id":"t10","time": "2023-01-15T10:55:00.000", "temp": 75.232},

            {"id":"t1", "time": "2023-01-15T11:00:00.000", "temp": 18.432},
            {"id":"t2", "time": "2023-01-15T11:00:00.000", "temp": 18.672},
            {"id":"t3", "time": "2023-01-15T11:00:00.000", "temp": 19.245},
            {"id":"t4", "time": "2023-01-15T11:00:00.000", "temp": 24.223},
            {"id":"t5", "time": "2023-01-15T11:00:00.000", "temp": 35.232},
            {"id":"t6", "time": "2023-01-15T11:00:00.000", "temp": 37.232},
            {"id":"t7", "time": "2023-01-15T11:00:00.000", "temp": 72.987},
            {"id":"t8", "time": "2023-01-15T11:00:00.000", "temp": 74.232},
            {"id":"t9", "time": "2023-01-15T11:00:00.000", "temp": 76.232},
            {"id":"t10","time": "2023-01-15T11:00:00.000", "temp": 75.232}
    ]
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
