from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    guest_id = Column(String, index=True)
    comment = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
