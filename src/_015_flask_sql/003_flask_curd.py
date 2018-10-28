from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json,logging


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


## 生成的表名是user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

  
    @classmethod
    def serialize(cls,_usr):
        return {
            "id": _usr.id,
            "username": _usr.username,
            "email": _usr.email
        }  

def insert_tuff():
    db.create_all()
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    all_result = User.query.all()
    for r in all_result:
        print('user name is %s and user email is %s ' % (r.username,r.email))
    u = User.query.filter_by(username='admin').first()  
    print('name is %s and email is %s' % (u.username,u.email)) 

def main():
    insert_tuff()
    app.run(debug=True)    


@app.route('/user/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    # return render_template('show_user.html', user=user)
    user_ = {'name':user.username,'email':user.email}
    ## peter = User.query.filter_by(username='peter').first()

    ##missing = User.query.filter_by(username='missing').first()
    all_users = User.query.filter(User.email.endswith('@example.com')).all()
    # User.query.order_by(User.username).all()
    # User.query.limit(1).all()
    # User.query.get(1)
    result = None
    try:
        result = json.dumps(all_users,default=User.serialize)
    except (AttributeError,TypeError) as e:
        logging.error("formating json obj error! \n   root cause %s" % e)
        result = json.dumps({"status_code":403,"error_msg":"json serialize error!"})
    return result


@app.route("/")
def home():
    return "My flask app"


if __name__ == '__main__':
    main() 