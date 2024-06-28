#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Ses = sessionmaker(bind=engine)
    ses = Ses()

    nState = State(name='California')
    nCity = City(name='San Francisco')
    nState.cities.append(newCity)

    ses.add(newState)
    ses.add(newCity)
    ses.commit()
