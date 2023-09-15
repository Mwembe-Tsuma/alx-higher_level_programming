#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
"""
    Module that creates States class.
"""

Base = declarative_base()


class State(Base):
    """
        Class representing the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
