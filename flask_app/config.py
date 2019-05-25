import os

_DB_USER = os.environ.get("DB_USER")
_DB_NAME = os.environ.get("DB_NAME")

SQLALCHEMY_DATABASE_URI = f"postgres://{_DB_USER}@app-db/{_DB_NAME}"

SQLALCHEMY_TRACK_MODIFICATIONS = False

REDIS_DATABASE_URI = os.environ.get("REDIS_HOST")
