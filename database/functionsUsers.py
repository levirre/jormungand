from database.models import User
from flask import session
from sqlalchemy import inspect
from werkzeug.security import check_password_hash, generate_password_hash
from database.makedb import metadata, db_session, close_session, commit_session

def existing_user(name,password):
        uname = User.query.filter_by(username=name).first()

        #print(uname.username, uname.hash)
        #print(uname.__repr__())
        if uname is not None and name == uname.username :
            if check_password_hash(uname.hash,password):
                state = inspect(uname)
                print(f"State : {state.persistent}")
                
                #session['USER'] = uname.username
                #print(session['USER'])
                #db_session.remove()
                return True
        else:
                
            
            return False
def new_user(name,password):
    uname = User.query.filter_by(username=name).first()
    if uname == None:
        db_session.add(User(username=name,hash=password))
        commit_session()
        #db_session.remove()
        #engine.dispose()
        return True
        #session.add(users(username=user,hash=password))
    #else:
        #db_session.remove()
            #engine.dispose()

#print(existing_user('a2','a2'))
#db = get_db()
