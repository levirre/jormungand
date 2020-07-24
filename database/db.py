import os
from sqlalchemy import MetaData, Table, create_engine
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from werkzeug.security import check_password_hash
from flask import flash


def db():
    load_dotenv(find_dotenv())
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    #print(engine.table_names())
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    user=Base.classes.users
    Session = sessionmaker(bind=engine)
   # print(user)
    
      
    
def new_user(name,password):
    load_dotenv(find_dotenv())
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    #print(engine.table_names())
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    user=Base.classes.users
    Session = sessionmaker(bind=engine)
    session = Session()
    uname = session.query(user).filter_by(username=name).first()

    
    if uname == None:
        session.add(user(username=name,hash=password))
        session.commit()
        flash('Registered')
    #session.add(users(username=user,hash=password))
    else:
        session.close()
        engine.dispose()
        print('Try again')
        

def existing_user(name,password):
    load_dotenv(find_dotenv())
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    #print(engine.table_names())
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    user=Base.classes.users
    Session = sessionmaker(bind=engine)
    session = Session()
    uname = session.query(user).filter_by(username=name).first()
    
    if uname:
        if check_password_hash(uname.hash,password):
            print('wew')
            session.close()
            engine.dispose()
        else:
            print('no')
    return 

            


        
    #if uname != None:



#session.query(hentai).filter(hentai.name =='Junyoku Kaihouku').delete()
#session.add(hentai(id="297807",name="Junyoku Kaihouku"))
#session.commit()
#session.close()
#engine.dispose()



#'__abstract__', '__class__', '__delattr__',
#  '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__le__', '__lt__', '__mapper__', '__module__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', '__table__', '__weakref__', 
# '_decl_class_registry', '_sa_class_manager', '_sa_decl_prepare', 
# '_sa_raise_deferred_config', 'classes', 'id', 'metadata', 'name', 'prepare'


#session.add(hentai(id="297807",name="Junyoku Kaihouku"))
#session.commit()
#u1 = session.query(hentai).all()
#for u in u1:
#    print(u.id)
#session.close()
#engine.dispose()
###QUERY FROM SESSION INSTANCE USING AUTOMAP BASE REFLECTION
#u1 = session.query(hentai).all()
#for u in u1:
#    print(u.id)

###PRINT FROM ENGINE ONLY ###
#hen = engine.execute("SELECT * FROM hentai")
#for h in hen:
#    print(h['name'] + ": " + str(h['gallery']))
