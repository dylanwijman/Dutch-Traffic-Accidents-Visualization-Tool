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

PATH_TO_DATA = "verkeersOngelukkenNederlandProtocol2.p"
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
    # result = data[ (data["PVE_CODE"] == "NH") & (data["JAAR_VKL"] == 2015)]
    # return  result.head(3).reset_index().to_json(orient='index')

    result = data[ (data["JAAR_VKL"] == year)]
    output = result["PVE_NAAM"].value_counts().to_json(orient="columns")

    return output




if __name__ == "__main__":
    data = pickle.load(open( PATH_TO_DATA, "rb" ) )

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)






