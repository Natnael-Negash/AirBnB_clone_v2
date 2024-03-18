#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("city", cascade='all, delete, delete-orphan', backref="state")

    if getenv("HBNB_TYPE_STORAGE") !="db":
        @property
        def cities(self):
            """Return: list of related City objects"""
            list_of_city = []
            cities = list(models.storage.all(City).value())
            for city in cities:
                if city.state_id == self.id:
                    list_of_city.append(city)
            return list_of_city