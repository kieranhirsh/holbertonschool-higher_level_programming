#!/usr/bin/python3
""" the checker demands documentation """
import sys
from model_state import Base, State
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

    for row in session.query(State).where(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(row.id, row.name))
