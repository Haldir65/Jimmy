from conduit.database import Column,Model,SurrogatePK,db
from conduit.extensions import bcrypt


class Quote(SurrogatePK,Model):
    __tablename__ = 't_quotes'

    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(2000),nullable=False) ## quoto contents 
    user_id = db.Column(db.Integer,
        db.ForeignKey('t_user.id'),nullable =False)
