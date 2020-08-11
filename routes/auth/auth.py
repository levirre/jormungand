from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
)
import sys
from werkzeug.exceptions import abort
#from database.db import new_user, existing_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session as sess
from database.models import User
from database import functionsUsers, makedb
from sqlalchemy import inspect
import time


reg= Blueprint('reg',__name__,url_prefix='/user')
home=Blueprint('home',__name__)



@home.route('/',methods=['GET'])
def index():
    retry=''
    return redirect(url_for('reg.login'))

@home.route('/profile/<user>',methods=['GET'])
def profile(user):
    
    if 'USER' in sess:
        g.user = sess['USER']
        return render_template('home.html')
    else:
        return redirect(url_for('reg.login'))

@reg.route('/register',methods=(['GET','POST']))
def register():
    
    if request.method =='POST':
        #db()
        username = request.form['user']
        password = request.form['hash']
        password = generate_password_hash(password)
        if functionsUsers.new_user(username,password):
            return redirect(url_for('.login'))
        else:
            retry='name taken'
            return render_template('register.html',retry=retry)
    else:
        return render_template('register.html')

@reg.route('/login',methods=(['GET','POST']))
def login():
    start = time.time()
    if request.method =='POST':
        username = request.form['user']
        password = request.form['hash']
        if functionsUsers.existing_user(username,password):
            sess['USER'] = username
            end = time.time()
            print(end - start)
            g.user = sess['USER']
            flash('You were successfully logged in')
            return redirect(url_for('home.profile',user=g.user))
        else:
            return redirect(url_for('.loser'))
    return render_template('login.html')

@reg.route('/logout',methods=(['GET']))
def logout():
    sess.pop('USER', None)
    return redirect(url_for('home.main'))

@reg.route('/winner',methods=(['GET']))
def winner():
    return "winner"

@reg.route('/loser',methods=(['GET']))
def loser():
    return "loser"

