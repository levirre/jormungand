#
started = False;
#import os
#from dotenv import load_dotenv, find_dotenv
while True:
    c=input(">")
    if c == "start":
        if started==True:
            print("car already started")
        else:
            started=True;
            print ("car start")
    elif c == "stop":
        if started==False:
            print("car already stopped")
        else:
            started=False;
            print ("car stop")
    else:
        break;

#class Config(object):
#    load_dotenv(find_dotenv())
#    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
#engine = create_engine('postgresql+psycopg2://lev:1234@localhost:5433/lolidb')
#print(engine.table_names())
#load_dotenv(find_dotenv())
#print(os.getenv("DATABASE_URL"))

#TODO: connect config.py to __init__
    # print table names
    #how to create the local db in python
    #connect db with app
    #migrate db to heroku
