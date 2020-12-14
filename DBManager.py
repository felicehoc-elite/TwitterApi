from typing import Type

import mysql.connector


class MySqlDBManager:


    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None


    def connect(self):
        self.connection = mysql.connector.connect(self.host, self.user, self.password, self.database)
        self.connection.autocommit = False

    def close(self):
        self.connection.close()
