#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Ses = sessionmaker(bind=engine)
    ses = Ses()

    states = ses.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        ses.delete(state)

    ses.commit()
