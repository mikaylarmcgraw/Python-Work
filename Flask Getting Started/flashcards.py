from flask import Flask, jsonify, request, render_template, abort
from flask_cors import CORS
from datetime import datetime
from model import db

# Each method needs to have a unique name for a web app in flask or it will give you an error.

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET', 'POST'])
def welcome():
    return render_template("welcome.html",
                           message="Here's a message from the view.")


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route("/date")
def date():
    return"this is another method call." + str(datetime.now())


counter = 0


@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "this page was served " + str(counter) + " times"
