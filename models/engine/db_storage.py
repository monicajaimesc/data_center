#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.state import State
from os import getenv
from sqlalchemy import create_engine


classe = {"State": State}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def get(self, cls, id):
        """
        Gets a result from DBStorage
        """
        data = self.all(cls)
        try:
            value = data['{}.{}'.format(cls, id)]
        except KeyError:
            value = None

        return value

    def count(self, cls=None):
        """
        Count the number of ocurrences from DB storage
        """
        if cls is None:
            data = self.all()
        else:
            data = self.all(cls)

        return len(data)