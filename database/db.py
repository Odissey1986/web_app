from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DB_URL = "sqlite:///./database.db"

engine = create_engine(DB_URL)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()