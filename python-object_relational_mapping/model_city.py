#!/usr/bin/python3
""" the checker demands documentation """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """
    The city class
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    state_id = Column(Integer, ForeignKey(State.id))
    name = Column(String(128), nullable=False)
