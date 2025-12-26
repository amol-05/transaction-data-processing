# this is an entity file

from sqlalchemy import Column, Integer, String, Date
from src.db.base import Base

class Customer(Base):
    __tablename__ = "customers" # This is table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    date_of_birth = Column(Date, nullable=True)


