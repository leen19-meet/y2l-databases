from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    # TODO: complete this class
    __tablename__ = 'Product'
    id=Column(Integer,primary_key=True)
    price =Column(Integer)
    quantity= Column(Integer)
    description= Column(String)
    country= Column(String)
    last= Column(String)


