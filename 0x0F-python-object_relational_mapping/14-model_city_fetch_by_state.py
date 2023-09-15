#!/usr/bin/python3
"""
script that contains the class definition of a City
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
