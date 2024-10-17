# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Define the base class
Base = declarative_base()

class Philosopher(Base):
    """description: Table to store philosophers."""
    __tablename__ = 'philosopher'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    nationality = Column(String)

class Quote(Base):
    """description: Table to store quotes attributed to philosophers."""
    __tablename__ = 'quote'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False)
    philosopher_id = Column(Integer, ForeignKey('philosopher.id'), nullable=False)

class Category(Base):
    """description: Table to store categories for quotes."""
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class QuoteCategory(Base):
    """description: Junction table to map quotes to categories (many-to-many relationship)."""
    __tablename__ = 'quote_category'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    quote_id = Column(Integer, ForeignKey('quote.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

# Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample data insertion
philosopher_1 = Philosopher(name="Socrates", birth_date=datetime.datetime(470, 1, 1), nationality="Greek")
philosopher_2 = Philosopher(name="Friedrich Nietzsche", birth_date=datetime.datetime(1844, 10, 15), nationality="German")

quote_1 = Quote(text="The only true wisdom is in knowing you know nothing.", philosopher_id=1)
quote_2 = Quote(text="Without music, life would be a mistake.", philosopher_id=2)
quote_3 = Quote(text="He who has a why to live can bear almost any how.", philosopher_id=2)

category_1 = Category(name="Wisdom")
category_2 = Category(name="Existence")

quote_category_1 = QuoteCategory(quote_id=1, category_id=1)
quote_category_2 = QuoteCategory(quote_id=3, category_id=2)

# Add and commit new records to the database
session.add_all([
    philosopher_1, philosopher_2,
    quote_1, quote_2, quote_3,
    category_1, category_2,
    quote_category_1, quote_category_2
])

session.commit()
