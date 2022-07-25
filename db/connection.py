import pymysql.cursors
import pymysql
from constants.db import params


class Connection:

    @classmethod
    def init_db(self):
        self.__connection = pymysql.connect(
            cursorclass=pymysql.cursors.DictCursor, **params)
        self.__cursor = self.__connection.cursor()

    @classmethod
    def get(self, query, params):
        self.__cursor.execute(query, params)
        return self.__cursor.fetchall()


Connection.init_db()
