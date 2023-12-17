#!/usr/bin/python3
"""
Script to create State "California" with City "San Francisco" using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name))

    # Create tables
    Base.metadata.create_all(engine)

    # Create a new State "California" with City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Create a session and add the State and City to the database
    session = Session(engine)
    session.add(new_state)
    session.commit()
    session.close()
