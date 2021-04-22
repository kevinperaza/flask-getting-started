from flask import Flask, render_template, abort, jsonify, request, redirect
from flask.globals import request
from flask.helpers import url_for
from model import db, save_db

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

@app.route("/cards/create", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # process data
        db.append(dict(request.form.to_dict(), **{"index": len(db) -1}))
        save_db()
        return redirect(url_for("card_view", index=len(db) -1))
    else:
        return render_template("create_card.html")

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