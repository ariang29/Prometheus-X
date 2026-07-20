from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database.database import Base

class Research(Base):
    __tablename__ = "research"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String(500), nullable=False)
    report = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
