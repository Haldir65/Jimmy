from flask import Blueprint
from _module1.models import Product

blueprint = Blueprint('model1', __name__)


@blueprint.route('/',methods=['GET'])
def index():
    return json.dumps({"msg":"dumb ass1","code":0})