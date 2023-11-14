from . import db


class Purchases(db.Model):
    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    quantity = db.Column(db.Integer, nullable=False)

    event = db.relationship('Events', backref='purchases')
    client = db.relationship('Clients', backref='purchases')