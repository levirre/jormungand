from flask import Flask, render_template
from database.db import db
from flask import request

app = Flask(__name__)


#@app.route('/')
#def index():
#    return render_template('home.html')

@app.route('/',methods=(['GET','POST']))
def register():
    if request.method =='POST':
        username = request.form['user']
        password = request.form['hash']
        db(username,password)
        return render_template('home.html')
    else:
        return render_template('login.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1')

