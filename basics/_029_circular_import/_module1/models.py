from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey

from database import db


class Product(db.Model):
    __tablename__="t_product"
    __table_args__ = {"useexisting": True}
    prod_id = db.Column(db.Integer, primary_key=True)
    prod_desc = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return '<Product  %r>' % self.prod_desc


