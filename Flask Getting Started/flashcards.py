from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

# Each method needs to have a unique name for a web app in flask or it will give you an error.

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET', 'POST'])
def welcome():
    return "You are successfully connected to flask app"


@app.route("/date")
def date():
    return"this is another method call." + str(datetime.now())


counter = 0


@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "this page was served " + str(counter) + " times"
