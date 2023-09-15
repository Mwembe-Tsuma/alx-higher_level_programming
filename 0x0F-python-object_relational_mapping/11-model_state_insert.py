#!/usr/bin/python3
"""
script that adds the State object Louisiana
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    add_st = State(name="Louisiana")
    session.add(add_st)

    session.commit()
    print(add_st.id)
    session.close()
