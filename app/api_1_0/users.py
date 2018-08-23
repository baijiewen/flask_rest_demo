from flask import request, jsonify, url_for
from app.models import User
from . import api
from .. import db


@api.route('/users/', methods=['POST'])
def new_user():
    name = request.form.get('name')
    sex = request.form.get('sex')
    telphone = request.form.get('telphone')
    user = User(name=name, sex=sex, telphone=telphone)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201, \
        {'Location': url_for('api.get_user', id=user.id)}


@api.route('/users/<int:id>', methods=['PUT'])
def put_user(id):
    user = User.query.get_or_404(id)
    import pdb;pdb.set_trace()
    if len(request.form) > 0:
        for key in request.form:
            user.key = request.form[key]
        db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json(),{'Location': url_for('api.get_user', id=user.id)})


@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())
