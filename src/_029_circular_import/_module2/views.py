from flask import Blueprint
from _module2.models import User
import json

from database import db

blueprint = Blueprint('model2', __name__)


@blueprint.route('/',methods=['GET'])
def index():
    all = db.query(User).all()
    result = [u.user_id for u in all]
    return json.dumps({"msg":"dumb ass2","code":0})