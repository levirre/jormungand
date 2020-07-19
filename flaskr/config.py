#

import os
from dotenv import load_dotenv, find_dotenv


class Config(object):
    load_dotenv(find_dotenv())
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#engine = create_engine('postgresql+psycopg2://lev:1234@localhost:5433/lolidb')
#print(engine.table_names())
#load_dotenv(find_dotenv())
#print(os.getenv("DATABASE_URL"))

#TODO: connect config.py to __init__
# print table names