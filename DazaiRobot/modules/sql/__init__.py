from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from DazaiRobot import DB_URI
from DazaiRobot import LOGGER as log

# Create a base class for the ORM models
BASE = declarative_base()

# Check and modify DB_URI if necessary
if DB_URI and DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)

# Function to start the database session
def start() -> scoped_session:
    if not DB_URI:
        log.error("DB_URI is not set or is None")
        raise ValueError("DB_URI is not set or is None")

    engine = create_engine(DB_URI, client_encoding="utf8")
    log.info("[PostgreSQL] Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    # Initialize the session
    SESSION = start()
    log.info("[PostgreSQL] Connection successful, session started.")
except Exception as e:
    log.exception(f"[PostgreSQL] Failed to connect due to {e}")
    raise
