#!/usr/bin/python3
"""
State class with relationship to City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")
