from flask import Flask
from modules.auth.auth import reg
#The gunicorn command expects the names of your application module or package 
#and the application instance within the module. If you use the application factory pattern, 
#you can pass a call to that:

#$ gunicorn "myproject:create_app()"

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['SECRET_KEY'] = 'my super secret key'
    app.register_blueprint(reg)

@app.route('/')
def index():
    return render_template('register.html')
    
    

#@app.route('/')
#def index():
#    return render_template('home.html')




    return app

