
import sys
sys.path.append('../')

from app import db

class Book(db.Model):
    __tablename__ = "mybooks"
    id = db.Column( db.Integer, primary_key=True, nullable=False,autoincrement = True)
    title = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "<Title: {}>".format(self.title)

    @classmethod
    def serialize(cls,_book):
        return {
            "id": _book.id,
            "title": _book.title
        } 