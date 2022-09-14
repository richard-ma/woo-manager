from . import db


class Site(db.Model):
    __tablename__ = 'sites'
    url = db.Column(db.String(128), primary_key=True)
    key = db.Column(db.String(128))
    secret = db.Column(db.String(128))
    version = db.Column(db.String(128))
    active = db.Column(db.Boolean, default=True)
