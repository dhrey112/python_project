from .database import Base

from sqlalchemy import Column, Integer, String

class Blog(Base):
    __tablename__ = "blogs_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

class User(Base):
    __tablename__ = "users_table"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String) 