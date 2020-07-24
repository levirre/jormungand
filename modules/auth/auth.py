from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import sys
from werkzeug.exceptions import abort
from database.db import db,new_user, existing_user
from werkzeug.security import check_password_hash, generate_password_hash
#load database & start session


reg= Blueprint('reg',__name__,url_prefix='/user')

@reg.route('/register',methods=(['GET','POST']))
def register():
    if request.method =='POST':
        db()
        username = request.form['user']
        password = request.form['hash']
        password = generate_password_hash(password)
        new_user(username,password)
        return render_template('home.html')
    else:
        flash('test')
        return render_template('register.html')

@reg.route('/login',methods=(['GET','POST']))
def login():
    if request.method =='POST':
        username = request.form['user']
        password = request.form['hash']
        if existing_user(username,password):
            print('This is error output', file=sys.stderr)
            print('This is standard output', file=sys.stdout)
        else:
            print('test', file=sys.stderr)
            print('This is standard output', file=sys.stdout)
    return render_template('login.html')

