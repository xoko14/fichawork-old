from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    hashed_password = Column("password", String)
    name = Column(String)

class Shift(Base):
    __tablename__ = "shifts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)

class ShiftEntry(Base):
    __tablename__ = "shift_entry"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    time_clock_in = Column(DateTime)
    time_clock_out = Column(DateTime)
    description = Column(String)
