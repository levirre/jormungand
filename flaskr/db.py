import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgres+psycopg2://lzgxgutolqgijg:e38480d8d46fb63d5847520bd400a497f9725ca0d22aef2853024e7467a813d9@ec2-3-215-83-17.compute-1.amazonaws.com:5432/d12k0ea5a0s7uv')

#engine = create_engine('postgresql+psycopg2://lev:1234@localhost:5433/lolidb')
print(engine.table_names())

