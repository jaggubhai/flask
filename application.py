from flask import Flask
from flask.ext.mongoengine import MongoEngine #adding mongo engine
#from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
   
    db.init_app(app) # creating the database within the application

    from user.views import user_app
    app.register_blueprint(user_app)   
 
    return app
