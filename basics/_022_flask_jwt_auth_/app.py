from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_HEADER_PREFIX'] = 'awesome'
jwt = JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

if __name__ == '__main__':
    app.run()

## curl -X POST http://127.0.0.1:5000/auth --header "Content-Type:application/json" --data '{"username":"user1","password":"abcxyz"}'    
## {
 ## "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzEyMTg0NTUsImlhdCI6MTUzMTIxODE1NSwibmJmIjoxNTMxMjE4MTU1LCJpZGVudGl0eSI6MX0.TPfb5Xwthbwnnf5P1LNB0o-CKiSis8VH0Db6JEotc9A"
##}
## curl -X GET http://127.0.0.1:5000/protected --header "Content-Type:apon" --header "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzEyMTg0NTUsImlhdCI6MTUzMTIxODE1NSwibmJmIjoxNTMxMjE4MTU1LCJpZGVudGl0eSI6MX0.TPfb5Xwthbwnnf5P1LNB0o-CKiSis8VH0Db6JEotc9A"
## User(id='1')