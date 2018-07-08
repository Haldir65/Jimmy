from flask import (Flask,request,jsonify,render_template)
import json
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (MetaData,Table)
from sqlalchemy.schema import CreateTable
from app.models import Book



project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


def create_table_if_not_exits():
    if not db.engine.dialect.has_table(db.engine,Book.__tablename__):
        db.create_all()
    else:
        print("table already exists")    

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.data:
        ## type(request) == bytes
        print('request data is %s' % request.data)
    if request.form:
        print('request form is %s ' % request.form)
    content = request.get_json()
    print(content)
    return "My flask app "

@app.route("/book", methods=["GET", "POST"])
def book():
    content = request.get_json()
    create_table_if_not_exits()
    book = Book(title=content.get("title","default"))
    db.session.add(book)
    db.session.commit()
    return json.dumps({"errorCode":0,"errorMsg":"Ok"})

@app.route("/books", methods=["GET"])
def books():
    books = Book.query.all()
    return json.dumps(books,default=Book.serialize,indent=2,ensure_ascii=False)

@app.route("/update_book", methods=["POST"])
def update():
    content = request.get_json()
    create_table_if_not_exits()
    oldtitle=content.get("title","default")
    newtitle=content.get("newtitle","default_new")
    book = Book.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    db.session.commit()
    return json.dumps({"errorCode":0,"errorMsg":"Ok"})

if __name__ == "__main__":
    app.run(debug=True,port=9876)