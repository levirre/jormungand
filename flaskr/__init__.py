from flask import Flask, redirect, url_for, session
import os
from routes.auth.auth import reg, home
from database.makedb import db_session
import logging
from sqlalchemy import inspect
from database.models import User
#The gunicorn command expects the names of your application module or package 
#and the application instance within the module. If you use the application factory pattern, 
#you can pass a call to that:

#$ gunicorn "myproject:create_app()"

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['SECRET_KEY'] = '\xb8\xdd\xf7~X\xce\x8f\x8aM\x12\x98\xb7$(\x1e\xa1>\x00\xe6+\xd9~\x84\x03'
    app.register_blueprint(reg)
    app.register_blueprint(home)
    
#@app.route('/')
#def index():
#    return render_template('home.html')
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        
        db_session.remove()
        
        app.logger.info("called")
    return app

#@app.teardown_appcontext
#def shutdown_session(exception=None):
#    db_session.remove()

