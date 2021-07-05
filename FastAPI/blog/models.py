from sqlalchemy.sql.functions import user
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users_table.id'))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String) 

    blogs = relationship("Blog", back_populates="creator")