from sqlalchemy import DateTime, Integer, Column

from counter_app.database import Base

class Count(Base):
    __tablename__ = "counts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
