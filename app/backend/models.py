from database import base, engine, session_local
from sqlalchemy import Column, String, Integer

class Records(base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    name = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    rating = Column(String)
