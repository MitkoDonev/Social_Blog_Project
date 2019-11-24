# this imports from the blog file the initialized app variable
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

########################
#### DATABASE SETUP ####
########################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

########################
#### Login SETUP #######
########################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

##########################
#### BLUEPRINT IMPORT ####
##########################

from blog.core.views import core
from blog.users.views import users
from blog.blog_posts.views import blog_posts
from blog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)

if __name__ == '__main__':
    app.run(debug=True)
