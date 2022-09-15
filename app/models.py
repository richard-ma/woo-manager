from . import db


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(128), unique=True, index=True)
    key = db.Column(db.String(128))
    secret = db.Column(db.String(128))
    version = db.Column(db.String(128))
    active = db.Column(db.Boolean, default=True)

    def active_store(self):
        self.active = True

    def deactive_store(self):
        self.active = False
