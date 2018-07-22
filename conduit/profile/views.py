from flask import Blueprint,jsonify
from flask_jwt import current_identity,jwt_required


from .serializers import profile_schema,profile_schemas

from conduit.user.models import User
from conduit.exceptions import InvalidUsage
from conduit.utils import jwt_optional


from conduit.profile.models import UserProfile

blueprint = Blueprint("profile",__name__)


@blueprint.route('/api/profiles/<username>',methods=('GET',))
def get_profile(username):
    user = User.query.filter_by(username=username).first()
    profile = user.profile
    result = profile_schema.dump(profile).data
    print(result)
    if not user:
        raise InvalidUsage.user_not_found()
    return jsonify(result),200



