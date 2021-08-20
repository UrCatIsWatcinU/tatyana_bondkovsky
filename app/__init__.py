from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config())

login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

app.jinja_env.globals['service_name'] = 'Татьяна Бондковская'

from app import routes, models, admin