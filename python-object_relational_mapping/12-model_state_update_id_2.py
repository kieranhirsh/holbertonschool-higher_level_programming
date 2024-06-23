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
    
    modified_state = session.query(State).where(State.id == 2).first()
    modified_state.name = "New Mexico"
    session.add(modified_state)
    session.commit()
