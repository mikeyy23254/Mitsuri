import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = os.getenv('DB_URI')

if not DB_URI:
    raise ValueError("DB_URI environment variable is not set")

def start():
    engine = create_engine(DB_URI, client_encoding="utf8")
    Session = sessionmaker(bind=engine)
    return Session()

SESSION = start()
