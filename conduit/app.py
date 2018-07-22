from flask import Flask
from conduit.exceptions import InvalidUsage
from conduit.setting import Config

## 下面这两行换一下顺序就会变成循环import
from conduit.extensions import db,bcrypt,jwt
from conduit import user,profile,articles

def create_app(config_obj=Config):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    register_extensions(app)
    register_blueprint(app)
    return app


def register_blueprint(app):
    app.register_blueprint(user.views.blueprint)


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    jwt.init_app(app)


## for creating table issue
def create_table():
    app = create_app()
    app.app_context().push()
    db.create_all()

