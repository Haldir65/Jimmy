import datetime as dt

from flask_jwt import _default_jwt_encode_handler


from conduit.database import Column,Model,SurrogatePK,db
from conduit.extensions import bcrypt

class User(SurrogatePK,Model):

    __tablename__ = 't_user'
    username =Column(db.String(80),unique=True,nullable=False)
    email = Column(db.String(100),unique=True,nullable=False)
    password = Column(db.Binary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    bio = Column(db.String(300), nullable=True)
    image = Column(db.String(120), nullable=True)


    def __init__(self,username,email,password=None,**kwargs):
        db.Model.__init__(self,username=username,email=email,**kwargs)
        if password:
            self.set_password(password)
        else:
            self.password =None

    def set_password(self,password)            :
        self.password = bcrypt.generate_password_hash(password)


    def check_password(self,value):
        return bcrypt.check_password_hash(self.password,value)    


    @property
    def token(self):
        return _default_jwt_encode_handler(self).decode('utf-8')

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)    





