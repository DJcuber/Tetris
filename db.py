import mysql.connector
class Database:
    def __init__(self, main):
        self.main: object = main
        self.conn: object = None
        self.cursor: object = None
        self.user: int = -1
        self.connect()
        
    def connect(self) -> None:
        try:
            #attempts to connect to the database
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd="", database = "Tetris")
            self.cursor = self.conn.cursor()
        except:
            print("Couldn't connect to database")
            quit()
            
    def search(self, query) -> list[tuple]:
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def mutate(self, query) -> None:
        self.cursor.execute(query)
        self.conn.commit()
