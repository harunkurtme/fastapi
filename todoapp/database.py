from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_URL="sqlite:///./todo.db"


engine =create_engine(
    database_URL,connect_args={
        "check_same_thread":False
    }
)

sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
