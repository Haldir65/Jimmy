from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey

from databse import db

class Student(db.Model):
    __tablename__="t_student"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    studentname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)


class Course(db.Model):
    __tablename__="t_course"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    course_name = db.Column(db.String(80), nullable=False)
    course_price = db.Column(db.Integer, default=0)


class Person(db.Model):
    __tablename__="t_person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='t_person', lazy=True)

class Address(db.Model):
    __tablename__="t_adress"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('t_person.id'),
        nullable=False)    
