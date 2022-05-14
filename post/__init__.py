from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

app.config['SECRET_KEY'] = '123456789'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from post import views