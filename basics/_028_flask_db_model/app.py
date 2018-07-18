from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json
from database import init_app,db
import logging


app = Flask(__name__)
app.config.from_object('config')



@app.route('/',methods=['GET','POST'])
def index():
    return "dumb ass"



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()