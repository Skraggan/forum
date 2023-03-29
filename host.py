from db_connector import DatabaseConnector
from server import Server

db_connector = DatabaseConnector()
server = Server("localhost", 5000)
