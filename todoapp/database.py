from sqlite3 import connect
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#for heroku

SQL_ALCHEMY_URL=os.environ.get("DATABASE_URL")
if SQL_ALCHEMY_URL.startswith("postgres://"):
    SQL_ALCHEMY_URL=SQL_ALCHEMY_URL.replace("postgres://","postgressql://",1)


engine =create_engine(
 SQL_ALCHEMY_URL
 )

# for local
database_URL="sqlite:///./todo.db"


engine =create_engine(
    database_URL,connect_args={
        "check_same_thread":False
    }
)

sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

base =declarative_base()
