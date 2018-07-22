from flask import Blueprint,jsonify,Response,request
import json
from conduit.qutotes.models import Quote


blueprint = Blueprint('quotes',__name__)


@blueprint.route('/api/quotes/<int:userId>',methods=('GET',))
def get_quotes_by_user_id(userId):
    quotes = Quote.query.filter_by(user_id=userId).all()
    if(quotes is None or len(quotes)==0):
        return jsonify({"msg":"no record found"}) , 200
    else:
        results = [q.content for q in quotes]
        return jsonify(results),200
