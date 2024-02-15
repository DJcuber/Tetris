import mysql.connector
import hashlib

class LogIn:
    def __init__(self, main):
        self.main = main
        self.main.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.main.conn = mysql.connector.connect(host="localhost", user="root", passwd="", database = "Tetris")
            self.main.cursor = self.main.conn.cursor()
            self.cursor = self.main.cursor
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
        while True:
            user = input("Username: ")
            passwd = input("Password: ")
            passwd = hashlib.sha256(bytes(passwd, "utf-8")).hexdigest()

            self.cursor.execute(f"SELECT playerID, userName, passHash FROM player WHERE userName = '{user}'")
            data = self.cursor.fetchall()
            if not(data):
                print("User not found")
            elif data[0][2] == passwd:
                self.main.user = data[0][0]
                self.main.mode = "menu"
                return 
                #login
            else:
                print("Incorrect password")
           

    def createUser(self):
        self.cursor.execute("SELECT userName FROM player")
        usernames = self.cursor.fetchall()
        taken = False
        name = input("Enter a username between 1-32 characters\n")
        for user in usernames:
            if user[0] == name:
                taken = True
                print("Username taken")
                break
        #get users from database and validate
        while not(1 <= len(name) <= 32) or taken:
            taken = False
            name = input("Enter a username between 1-32 characters\n")
            for user in usernames:
                if user[0] == name:
                    taken = True
                    print("Username taken")
                    break
        passwd = input("Enter a password\n")
        passwd = hashlib.sha256(bytes(passwd, "utf-8")).hexdigest()
        self.cursor.execute(f"INSERT INTO player(userName, passHash) VALUES (\"{name}\", \"{passwd}\");")
        self.main.conn.commit()
        return self.menu()

        
class Stub:
    def __init__(self):
        pass

if __name__ == "__main__":
    inst = LogIn(Stub())
    inst.connect()
    inst.menu()
        
    
            

