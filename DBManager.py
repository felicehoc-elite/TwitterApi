from typing import Type

import mysql.connector


class MySqlDBManager:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
         self.connection = mysql.connector.connect(host = self.host, user = self.user, password = self.password, database = self.database)
         self.connection.autocommit = False

    def close(self):
        self.connection.close()
