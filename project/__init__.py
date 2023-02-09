from flask import Flask
from project.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
login = LoginManager(app)
#Redirect an anonymous user to the login route in order to access the desired page
login.login_view = 'login'


# Secret key
app.config.from_object(Config)


# Db configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initializing Sqlalchemy and migrate extensions
db = SQLAlchemy()
migrate = Migrate(app, db)
