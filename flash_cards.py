from flask import Flask, render_template, abort, jsonify
from model import db

app = Flask(__name__)

# SSR 

@app.route("/")
def welcome():
    return render_template("welcome.html", cards=db)


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db) - 1 )
    except IndexError:
        return abort(404)

# API

@app.route("/api/cards/")
def card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>")
def card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)