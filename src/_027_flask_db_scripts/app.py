from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json
from flask_script  import Manager
from flask_migrate  import Migrate, MigrateCommand
from databse import init_app,db
from models import Student
from serializer import serialize_student
import logging
app = Flask(__name__)
app.config.from_object('config')
manager = init_app(app)



@app.route('/',methods=['GET','POST'])
def index():
    return "dumb ass"


@app.route('/student',methods=['GET','POST'])
def student_insert():
    if request.data:
        data = json.loads(request.data)
        name = data.get('name',None)
        email = data.get('email',None)
        try:
            tim = Student(studentname=name,email=email)
            db.session.add(tim)
            db.session.commit()
        except Exception as e:
            logging.error(e)
            db.session.rollback()
            db.session.flush()
        id = None
        if tim:
            id = tim.id
        result = Student.query.filter_by(id=id).first()
        return json.dumps(result,default=serialize_student)
    return "invalid input"



@app.route('/student_list',methods=['GET'])
def student_list():
    results = Student.query.filter(Student.studentname != "tim").all()
    return json.dumps(results,default=serialize_student)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()