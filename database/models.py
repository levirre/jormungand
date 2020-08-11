from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from database.makedb import metadata, db_session, close_session
from sqlalchemy import inspect
from werkzeug.security import check_password_hash, generate_password_hash


class User(object):
    query = db_session.query_property()

    def __init__(self, username=None, hash=None):
        self.username = username
        self.hash = hash

    def __repr__(self):
        return (f"{self.username} %  {self.hash}")
    

users = Table('users', metadata,
    Column('username', String(50), primary_key=True),
    Column('hash', String(250), unique=True),
)
mapper(User, users)

#print(state.transient)
#print(state.pending)
#print(state.detached)
#print(state.persistent)
#print(User.existing_user('a2','a1'))

    



