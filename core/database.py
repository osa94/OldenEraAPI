from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

if SQLALCHEMY_DATABASE_URL is not None:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    raise ValueError("SQLALCHEMY_DATABASE_URL environment variable not defined")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()















#Base.metadata.tables['units_hive'].drop(engine)
#Base.metadata.tables['passive_abilities'].drop(engine)

