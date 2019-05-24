from datetime import datetime
import sqlalchemy.dialects.postgresql as pg

from app import db


class Event(db.Model):
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)
    price = db.Column(pg.MONEY, nullable=False)

    name = db.Column(db.String(128), nullable=False, index=True)

    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modified_on = db.Column(
        db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )
