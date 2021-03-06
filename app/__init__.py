from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()

#初始化flask_login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.login'

def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)


    #附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/user')


    return app