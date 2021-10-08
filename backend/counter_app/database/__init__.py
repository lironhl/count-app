from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from yashish.utils.constants import DB_PASSWORD, DB_URL, DB_USERNAME

engine = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/postgres", pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
