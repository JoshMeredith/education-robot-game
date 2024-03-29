from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, static_url_path='/static')

# FIXME(junkbot): Derive config from default / environment variable.
app.config.from_object('config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from web import views, models
from web.models import User
from web.forms import UsernamePasswordForm

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

app.jinja_env.globals.update(UsernamePasswordForm=UsernamePasswordForm)

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()

