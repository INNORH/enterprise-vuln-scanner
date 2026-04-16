from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy database engine
DATABASE_URL = "sqlite:///enterprise_vuln_scanner.db"
engine = create_engine(DATABASE_URL)

# Base model for ORM
Base = declarative_base()

# Session management
def get_db_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()

# Example Base model
class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))

# Create tables
Base.metadata.create_all(engine)