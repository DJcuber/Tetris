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

            self.cursor.execute("SELECT playerID, userName, passHash FROM player")
            data = self.cursor.fetchall()
            for i in data:
                if i[1] == user:
                    if i[2] == passwd:
                        pass
                        self.main.user = i[0]
                        self.main.mode = "menu"
                        return 
                        #login
                    else:
                        print("Incorrect password")
                        break
            else:
                print("User not found")
        

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
        return self.menu()

        
class Stub:
    def __init__(self):
        pass

if __name__ == "__main__":
    inst = LogIn(Stub())
    inst.connect()
    inst.menu()
        
    
            

