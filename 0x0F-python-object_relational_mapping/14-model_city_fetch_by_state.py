#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Ses = sessionmaker(bind=engine)
    ses = Ses()

    st_cty = ses.query(State, City).filter(State.id == City.state_id).all()

    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
