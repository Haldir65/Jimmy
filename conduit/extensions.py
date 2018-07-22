from flask_sqlalchemy import SQLAlchemy, Model
from flask_jwt import JWT
from flask_bcrypt import Bcrypt




class CRUDMixin(Model):

    @classmethod
    def create(cls,**kwargs):
        instance = cls(**kwargs)
        return instance.save()


    def update(self,commit=True,**kwargs):
        for attr,value in kwargs.items():
            setattr(self,attr,value)
        return commit and self.save() or self    

    def save(self,commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self,commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


bcrypt = Bcrypt()
db = SQLAlchemy(model_class=CRUDMixin)


from conduit.utils import authenticate,jwt_identity
jwt = JWT(authentication_handler=authenticate, identity_handler=jwt_identity)