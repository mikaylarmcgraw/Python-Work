from flask import Flask, jsonify, request, render_template, abort, redirect, url_for
from flask_cors import CORS
from datetime import datetime
from model import db

# Each method needs to have a unique name for a web app in flask or it will give you an error.

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET', 'POST'])
def welcome():
    return render_template("welcome.html",
                           cards=db
                           )


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route('/recommendation', methods=["GET", "POST"])
def recommendations():
    if request.method == "POST":
        # form has been submitted, process data
        card = {"question": request.content_type,
                "answer": request.content_type}
        db.append(card)
        return "successful response POST call"
    else:
        return "success response from GET call"


@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # form has been submitted, process data
        card = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(card)
        return redirect(url_for('card_view', index=(len(db)-1)))
    else:
        return render_template("add_card.html")


@app.route("/api/card/")
def api_card_list():
    # must wrap a list with jsonify it's not allowed to return just a list of data in flask
    return jsonify(db)


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
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
