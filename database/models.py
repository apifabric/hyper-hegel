# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 17, 2024 16:18:02
# Database: sqlite:////tmp/tmp.2MUj3J74r5/hyper-hegel/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    """
    description: Table to store categories for quotes.
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    QuoteCategoryList : Mapped[List["QuoteCategory"]] = relationship(back_populates="category")



class Philosopher(SAFRSBaseX, Base):
    """
    description: Table to store philosophers.
    """
    __tablename__ = 'philosopher'
    _s_collection_name = 'Philosopher'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    nationality = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    QuoteList : Mapped[List["Quote"]] = relationship(back_populates="philosopher")



class Quote(SAFRSBaseX, Base):
    """
    description: Table to store quotes attributed to philosophers.
    """
    __tablename__ = 'quote'
    _s_collection_name = 'Quote'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    philosopher_id = Column(ForeignKey('philosopher.id'), nullable=False)

    # parent relationships (access parent)
    philosopher : Mapped["Philosopher"] = relationship(back_populates=("QuoteList"))

    # child relationships (access children)
    QuoteCategoryList : Mapped[List["QuoteCategory"]] = relationship(back_populates="quote")



class QuoteCategory(SAFRSBaseX, Base):
    """
    description: Junction table to map quotes to categories (many-to-many relationship).
    """
    __tablename__ = 'quote_category'
    _s_collection_name = 'QuoteCategory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    quote_id = Column(ForeignKey('quote.id'), nullable=False)
    category_id = Column(ForeignKey('category.id'), nullable=False)

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("QuoteCategoryList"))
    quote : Mapped["Quote"] = relationship(back_populates=("QuoteCategoryList"))

    # child relationships (access children)
