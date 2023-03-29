import mysql.connector

class DatabaseConnector:
    def __init__(self) -> None:    
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="forum")
        
        self.cursor = self.mydb.cursor()
        print("Connected to the database!")

    def fetchThreads(self): 
        self.cursor.execute("SELECT * FROM threads")
        result = self.cursor.fetchall()
        for x in result:
            print(x)