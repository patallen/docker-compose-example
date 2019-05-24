import os

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

SQLALCHEMY_DATABASE_URI = f"postgres://{DB_USER}@app-db/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

REDIS_DATABASE_URI = f"redis://redis-db"
