from flask import Blueprint

view = Blueprint("viewws")

@view.route('/')
def home():
        return render_template("index.html")