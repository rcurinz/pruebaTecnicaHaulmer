from . import db
from sqlalchemy import func

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    start_hour = db.Column(db.String(50))
    date = db.Column(db.String(50))
    place = db.Column(db.String(50))
    price = db.Column(db.Integer)
    tickets_max = db.Column(db.Integer)
    tickets_sold = db.Column(db.Integer)
    description = db.Column(db.String(200))
