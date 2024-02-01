import mysql.connector
import hashlib

class LogIn:
    def __init__(self, main):
        self.main = main
        #self.main.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd="", database = "Tetris")
        except:
            print("Database went :(")

    def menu(self):
        choice = input("1. Login\n2. Create User\n")
        while not(choice in ("1", "2")):
            choice = input("1. Login\n2. Create User\n")
        if choice == "1":
            return self.login()
        return self.createUser()
    
    def login(self):
        pass

    def createUser(self):
        name = input("Enter a username between 1-32 characters\n")
        #get users from database and validate
        while not(1 <= len(name) <= 32):
            name = input("Enter a username between 1-32 characters\n")
        passwd = input("Enter a password\n")
        passwd = hashlib.sha256(bytes(passwd, "utf-8")).hexdigest()
        
        

if __name__ == "__main__":
    inst = LogIn(None)
    inst.menu()
        
    
            

