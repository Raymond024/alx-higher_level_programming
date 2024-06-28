#!/usr/bin/python3
"""
Adds the State object "Lousiana" to the database
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

    newState = State(name='Louisiana')
    ses.add(newState)
    ses.commit()

    print(newState.id)
