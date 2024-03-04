import hashlib

class LogIn:
    def __init__(self, main) -> None:
        self.main: object = main
        self.menu()

    def menu(self) -> None:
        choice = input("1. Login\n2. Create User\n")
        while not(choice in ("1", "2")):
            choice = input("1. Login\n2. Create User\n")
        if choice == "1":
            return self.login()
        return self.createUser()
    
    def login(self) -> None:
        while True:
            user = input("Username: ")
            passwd = input("Password: ")
            passwd = hashlib.sha256(bytes(passwd, "utf-8")).hexdigest()

            data = self.main.db.search(f"SELECT playerID, userName, passHash FROM player WHERE userName = '{user}'")
            if not(data):
                print("User not found")
            elif data[0][2] == passwd:
                self.main.db.user = data[0][0]
                self.main.mode = "menu"
                print("Logged in")
                return None
                #login
            else:
                print("Incorrect password")
           

    def createUser(self) -> None:
        usernames = self.main.db.search("SELECT userName FROM player")
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
        self.main.db.mutate(f"INSERT INTO player(userName, passHash) VALUES (\"{name}\", \"{passwd}\");")
        return self.menu()

        
        
    
            

