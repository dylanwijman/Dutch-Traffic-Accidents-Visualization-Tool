"""
author: David Zomerdijk
Description: loads pickledata and makes importing data possible
"""

from flask import Flask
import pickle
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



if __name__ == "__main__":
    #data = pickle.load(open("Data/verkeersOngelukkenNederland.p", "rb"))
    app.run()