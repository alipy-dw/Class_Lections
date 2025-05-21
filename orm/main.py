from sqlalchemy import create_engine, column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#driver://user:password@host:port/db_name
db_url = 'postgresql://hello:1/@127.0.0.1:5432/orm_db'