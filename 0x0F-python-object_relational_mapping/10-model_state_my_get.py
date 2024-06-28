#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
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

    state = ses.query(State).filter(State.name == sys.argv[4]).first()
    print("Not found" if not state else state.id)
