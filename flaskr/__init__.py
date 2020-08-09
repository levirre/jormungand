from flask import Flask, redirect, url_for, session
import os
from routes.auth.auth import reg, home


#The gunicorn command expects the names of your application module or package 
#and the application instance within the module. If you use the application factory pattern, 
#you can pass a call to that:

#$ gunicorn "myproject:create_app()"

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['SECRET_KEY'] = 'my super secret key'
    app.register_blueprint(reg)
    app.register_blueprint(home)
    
#@app.route('/')
#def index():
#    return render_template('home.html')

    return app


#@app.teardown_appcontext
#def shutdown_session(exception=None):
#    db_session.remove()

