from flask import jsonify


def template(data,code=500):
    return {'message':{'error':{'body':data}},'status_code':code}

UKNOWN_ERROR = template([], code=500)
ARTICLE_NOT_FOUND = template(['Article not found'], code=404)


class InvalidUsage(Exception):
    status_code = 500

    def __init__(self,message,status_code=None,payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code:
            self.status_code = status_code
        if self.payload:
            self.payload = payload


    def to_json(self):
        res = self.message
        return jsonify(res)

    @classmethod
    def unknown_error(cls):
        return cls(**UKNOWN_ERROR)


    @classmethod
    def article_not_found(cls):
        return cls(**ARTICLE_NOT_FOUND)



