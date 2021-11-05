from flask import Blueprint,render_template

view = Blueprint("viewws")

@view.route('/')
def home():
        return render_template("index.html")