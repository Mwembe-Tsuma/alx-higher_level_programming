#!/usr/bin/python3
"""
script that prints the first State object from db
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    s = session.query(State).order_by(State.id).first()

    if s:
        print("{}: {}".format(s.id, s.name))
    else:
        print("Nothing")
    session.close()
