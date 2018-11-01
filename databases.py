from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(price, quantity, description, country, last):
  #TODO: complete the functions (you will need to change the function's inputs)
  product = Product(
    price=price,
    quantity= quantity,
    description= description,
    country= country,
    last= last)
  session.add(product)
  session.commit()


def update_product(id,price,quantity):
  #TODO: complete the functions (you will need to change the function's inputs)
  product = session.query(
    Product).filter_by(
      id=id).first()
  

def delete_product(id):
  session.query(Product).filter_by(
    id=id).delete()
  session.commit()


def get_product(id):
  pass
