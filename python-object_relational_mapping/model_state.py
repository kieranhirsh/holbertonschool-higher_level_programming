#!/usr/bin/python3
""" the checker demands documentation """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SomeClass(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name =  Column(String(128), nullable=False)