#!/usr/bin/python3
""" a script that lists only first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def main(argv):
    """ main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(str(instance.id) + ': ' + instance.name)
    session.close()


if __name__ == '__main__' and len(sys.argv) == 4:
    main(sys.argv)
