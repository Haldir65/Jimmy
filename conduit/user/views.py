from flask import Blueprint,request,Response,jsonify
from flask_jwt import current_identity,jwt_required
from flask_jwt import current_identity,jwt_required


from sqlalchemy.exc import IntegrityError

import json

from .models import User
from .serializers import user_schema,user_schemas
from conduit.profile.models import UserProfile

from conduit.database import db
from conduit.exceptions import InvalidUsage
from conduit.utils import jwt_optional




blueprint = Blueprint('user',__name__)


@blueprint.route('/api/users',methods=('POST',))
def register_user():
    data = request.get_json(silent=True)
    user_data = user_schema.load(data).data ##默认生成一个dict
    try:
        user = User(username=user_data.pop('username'),
        email=user_data.pop('email'),
        password=user_data.pop('password'),**user_data)
        user = user.save()
        user_profile = UserProfile(user).save()
    except IndentationError:
        db.session.rollback()
        raise InvalidUsage.unknown_error
    result = user_schema.dump(user_profile.user).data
    return Response(json.dumps(result),status=201)



@blueprint.route('/api/users/login', methods=('POST',))
@jwt_optional()
def login_user():
    data = request.get_json(silent=True)
    user_data = user_schema.load(data).data
    email = user_data.pop('email')
    password = user_data.pop('password')
    user = User.query.filter_by(email=email).first()
    if user is not None and user.check_password(password):
        # user_str = user_schema.dump(user).data
        print(user.token)
        print(user)
        return Response(user.token,200)
    else:
        raise InvalidUsage.user_not_found()

@blueprint.route('/api/user', methods=('GET',))
@jwt_required()
def get_user():
    print(current_identity.bio)
    data = user_schema.dump(current_identity).data
    print(data['user'].pop('token'))
    
    return jsonify(data),200



## get user by id
@blueprint.route('/api/user/<int:userId>', methods=('GET',))
@jwt_required()
def get_user_by_id(userId):
    user = User.query.filter_by(id=userId).first()
    if (user is None):
        result = {'msg':"user not found"}
        return jsonify(result),404
    else:
        result = user_schema.dump(user).data
        # data = user_schema.dump(current_identity).data
        print(result['user'].pop('token'))
        return jsonify(result),200






