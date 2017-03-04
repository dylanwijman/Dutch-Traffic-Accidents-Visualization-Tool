from flask import Flask, render_template, Response, make_response
from flask import jsonify
import redis
import random
import json
import pandas
import numpy as np

df = pandas.DataFrame({
    "x": [11, 28, 388, 400, 420],
    "y": np.random.rand(5)
})

d = [
    dict([
             (colname, row[i])
             for i, colname in enumerate(df.columns)
             ])
    for row in df.values
    ]
app = Flask(__name__)


@app.route('/streamdata')
def event_stream():
    list = {}
    list['2012'] = [12,34,65,76]
    return jsonify(list)


@app.route('/stream')
def show_basic():
    x = random.randint(0, 101)
    y = random.randint(0, 101)
    json.dumps(d)
    return render_template("redisd3.html", data=json.dumps(d))


if __name__ == '__main__':
    app.run(threaded=True,
            host='0.0.0.0'
            )