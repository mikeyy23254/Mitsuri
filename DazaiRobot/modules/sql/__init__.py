from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from DazaiRobot import DB_URI
from DazaiRobot import LOGGER as log

# Create a base class for the ORM models


# Check and modify DB_URI if necessary

# Function to start the database session
def start() -> scoped_session:
    engine = create_engine( "postgresql://hjvbfqlt:Nk6a2lXvBIW7obyFl8LcJTOiKI7YhCnC@berry.db.elephantsql.com/hjvbfqlt" , client_encoding="utf8")
    log.info("[PostgreSQL] Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=True))

BASE = declarative_base()
try:
    # Initialize the session

    SESSION = start()
    log.info("[PostgreSQL] Connection successful, session started.")
except Exception as e:
    log.exception(f"[PostgreSQL] Failed to connect due to {e}")
    raise
