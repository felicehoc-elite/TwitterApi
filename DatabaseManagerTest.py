from DBManager import MySqlDBManager


db_manager = MySqlDBManager(host = "localhost", user = "root", password = "", database = "twitterdb")
db_manager.connect()