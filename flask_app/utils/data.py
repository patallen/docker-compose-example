from sqlalchemy.exc import SQLAlchemyError

from models import Event


def list_events(db):
    events = db.session.query(Event)
    return [_marshal_event(e) for e in events], 200


def add_event(db, event_json):
    errors = []

    if not event_json.get('date'):
        errors.append("'date' is a required field.")

    if not event_json.get('name'):
        errors.append("'name' is a required field.")

    if errors:
        return {'errors': errors}, 400

    event = Event(
        name=event_json['name'],
        price=event_json.get('price', 0),
        date=event_json['date']
    )

    db.session.add(event)

    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        raise

    return _marshal_event(event), 200

def _marshal_event(event):
    return {
        'price': event.price,
        'id': event.id,
        'date': str(event.date),
        'name': event.name,
    }
