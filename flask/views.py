from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name='Stanley')


@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

#returning json instead of html
@views.route("/json")
def get_json():
    return jsonify({'name': 'Stan', 'coolness': 10})

#getting data 
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirect
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))