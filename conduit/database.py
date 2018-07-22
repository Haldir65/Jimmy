from sqlalchemy.orm import relationship

from .extensions import db

Column = db.Column
relationship = db.relationship
Model = db.Model


class SurrogatePK():
    __table_args__ = {'extend_existing':True}

    id = Column(db.Integer,primary_key=True)

    @classmethod
    def get_by_id(cls,record_id):
        if any(
            (isinstance(record_id,int),
                isinstance(record_id,str) and record_id.isdigit()
            )):
            return cls.query.get((int)(record_id))

        
    def reference_col(tablename,nullable=False,pk_name='id',**kwargs):
        return Column(db.ForeignKey('{0}.{1}'.format(tablename,pk_name)),
        nullable=nullable,**kwargs)



