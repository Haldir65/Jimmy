import os
from datetime import timedelta
from conduit.config import data_base_url


class Config():
    SQLALCHEMY_DATABASE_URI = data_base_url
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=True
    SECRET_KEY = "supper_secret_key"
    JWT_AUTH_HEADER_PREFIX = 'Token'
    JWT_AUTH_USERNAME_KEY = 'email'
    SERVER_NAME = "127.0.0.1:6000"
    DEBUG = True