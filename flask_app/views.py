from flask import Blueprint

bp = Blueprint(__name__, "bp")


@bp.route("/")
def index():
    return "Welcome to my baby name blog!"
