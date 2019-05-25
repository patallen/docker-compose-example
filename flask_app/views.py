from flask import Blueprint, request, jsonify

from app import redis, db
from utils.counter import hit_counted
from utils import data


bp = Blueprint(__name__, "bp")


@bp.route("/events", methods=["GET"])
@hit_counted(redis)
def get_events(view_count):
    events, status_code = data.list_events(db)

    return jsonify({
        'events': events,
        'view_count': view_count,
    }), status_code


@bp.route("/events", methods=["POST"])
def add_event():
    event, status_code = data.add_event(db, request.json)
    return jsonify(event), status_code
