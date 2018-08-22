from flask import url_for
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sex = db.Column(db.Boolean)
    telphone = db.Column(db.Integer)

    def __repr__(self):
        return '<Users %r>'% self.name

    def to_json(self):
        json_post = {
            'url': url_for('api.get_user', id=self.id),
            'name': self.name,
            'sex': self.sex,
            'telphone': self.telphone
        }
        return json_post

