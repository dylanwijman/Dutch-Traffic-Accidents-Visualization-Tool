"""
Remark: Some code has been copy pasted from tutorials.
https://github.com/dfm/flask-d3-hello-world/blob/master/app.py
"""
"""
"""
import json
import os
import flask
import numpy as np
import pandas as pd
import pickle

PATH_TO_DATA = "../../Data/verkeersOngelukkenNederland.p"
app = flask.Flask(__name__)


@app.route("/")
def index():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("home.html")


@app.route("/data")
@app.route("/data/<int:year>")
def data(year= 2015 ):
    result = accidentData[ (accidentData["JAAR_VKL"] == year)]
    output = result["PVE_NAAM"].value_counts().to_json(orient="columns")

    #here we add the population data
    outputDict = {}
    for key, value in json.loads(output).items():
        outputDict[key] = {"accidents": value, "per_capita": round((int(value) / populationData[key] ), 5)}

    return json.dumps(outputDict)



if __name__ == "__main__":
    # load accident data
    accidentData = pickle.load(open( PATH_TO_DATA, "rb" ) )
    # import population data
    with open("static/data/population.json") as f:
        populationData = json.load(f)


    port = 8000

    # Open a web browser pointing at the app.
    #os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)






