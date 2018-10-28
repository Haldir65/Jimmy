import datetime as dt
from marshmallow import Schema, fields,post_load
from marshmallow import pprint
from models import Factory,Product,Computer
import logging

class User(object):
        def __init__(self, name, email,**kwargs):
                self.name = name
                self.email = email
                if not 'created_at' in kwargs.keys():
                        self.created_at = dt.datetime.now()
                        logging.error('created at in dict')
                else:
                        logging.error('found created at in kwargs')
                        self.created_at = kwargs.get('created_at',dt.datetime.now())

        def __repr__(self):
                return '<User(name={self.name!r})>'.format(self=self)

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime() 

    @post_load
    def make_user(self, data):
        # data.pop('created_at')
        return User(**data)

def serialize_obj():
        user = User(name="Monty", email="monty@python.org")
        schema = UserSchema()
        result = schema.dump(user)
        pprint(result)   

        json_result = schema.dumps(user)
        pprint(json_result)       

def de_serialize_obj():
        user_data = {
        'created_at': '2014-08-11T05:26:03.869245',
        'email': u'ken@yahoo.com',
        'name': u'Ken'
        }
        schema = UserSchema()
        result = schema.load(user_data)
        # pprint(result)  
        print(type(result.data))

def serialize_multiple_objs():
        user1 = User(name="Mick", email="mick@stones.com")
        user2 = User(name="Keith", email="keith@stones.com")
        users = [user1, user2]
        schema = UserSchema(many=True)
        result = schema.dumps(users,many=True)  # OR UserSchema().dump(users, many=True)
        # pprint(result)
        print(result.data)


def main():
        # serialize_obj()  
        logging.error("start of deserializing objs")
        de_serialize_obj()
        serialize_multiple_objs()

        

if __name__ == '__main__':
        main()
