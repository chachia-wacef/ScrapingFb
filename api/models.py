from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import ARRAY

Base  = declarative_base()

class Fbdata(Base):
    __tablename__ = 'fbdata'
    id  = Column(Integer, primary_key=True, index=True)
    page_name = Column(String)
    date = Column(String)
    text = Column(String)
    reactions_nbr = Column(Integer)
    shares_nbr = Column(Integer)
    comments_nbr = Column(Integer)
    comments = Column(String)
    images_url = Column(ARRAY(String))
    videos_url = Column(ARRAY(String))