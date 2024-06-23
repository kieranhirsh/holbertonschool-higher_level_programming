#!/usr/bin/python3
""" the checker demands documentation """
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in (session.query(State, City)
                       .join(City, State.id == City.state_id).all()):
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
