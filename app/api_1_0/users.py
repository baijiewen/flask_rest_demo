from flask import request, jsonify, url_for
from app.models import User
from . import api
from .. import db


@api.route('/users/', methods=['POST'])
def new_user():
    name=request.data.get('name')
    sex=request.data.get('sex')
    telphone=request.data.get('telphone')
    user = User(name=name,sex=sex,telphone=telphone)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201, \
        {'Location': url_for('api.get_post', id=user.id)}


@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())
