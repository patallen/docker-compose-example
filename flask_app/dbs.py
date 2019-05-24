from redis import Redis
from flask_sqlalchemy import SQLAlchemy


def create_redis_db(host):
    return Redis(host=host)


def create_app_db(app):
    return SQLAlchemy(app)
