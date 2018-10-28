from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


## 生成的表名是user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

def main():
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


if __name__ == '__main__':
    main() 