from database.models import User
from flask import session
from sqlalchemy import inspect
from werkzeug.security import check_password_hash, generate_password_hash
from database.makedb import metadata, get_db, db_session, close_session

def existing_user(name,password):
        uname = User.query.filter_by(username=name).first()
        state = inspect(uname)
        print(f"State : {state.persistent}")
        #print(uname.username, uname.hash)
        #print(uname.__repr__())
        if name == uname.username:
            if check_password_hash(uname.hash,password):
                
                #session['USER'] = uname.username
                #print(session['USER'])
                db_session.remove()

                print(f"State : {state.persistent}")
                return True
            else:
                
                print(f"State : {state.persistent}")
                return False
def new_user(name,password):
    uname = User.query.filter_by(username=name).first()
    if uname == None:
        db_session.add(User(username=name,hash=password))
        db_session.commit()
        close_session()
        #engine.dispose()
        return True
        #session.add(users(username=user,hash=password))
    else:
        close_session()
            #engine.dispose()

print(existing_user('a2','a2'))
#db = get_db()
