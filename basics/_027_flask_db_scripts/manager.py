from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json
from flask_script  import Manager
from flask_migrate  import Migrate, MigrateCommand

from app import app
from databse import init_app
from models import Student


app.config.from_object('config')
manager = init_app(app)



def main():
    manager.run()
    # app.run(debug=True)

if __name__ == '__main__':
    main()