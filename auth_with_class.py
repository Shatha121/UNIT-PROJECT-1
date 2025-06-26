import json
import os

class Auth:
    def __init__(self):
        self.path = "D:/Units/UNIT-PROJECT-1/data/users.json"
        self.users = self.load_user()
    def load_user(self):
        if os.path.exists(self.path):
            with open(self.path,"r") as file:
                try:
                    users_dict = json.load(file)
                except json.JSONDecodeError:
                    users_dict = {}
        else:
            users_dict = {}
        return users_dict
    def save_user(self):
        with open(self.path,"w") as file:
            json.dump(self.users,file,indent=2)
    
    def login(self,username,password):
        if username in self.users:
            if self.users[username]["password"] == password:
                if self.users[username]["role"] == "admin":
                    return {"username":username,"role":"admin"}
                else:
                    return {"username":username,"role":"member"}
            else:
                raise ValueError("incorrect password!")
        else:
            raise ValueError("The username doesn't exist!")
        
    def register(self,username,password):
        access_code = "@superaccess123"
        if username in self.users:
            raise ValueError("The username already exists!")
        else:
            
            admin_or_member = input("Do you want to register as admin or member? ")
            if admin_or_member.lower() == "admin":
                checking_access = input("Enter admin access code: ")
                if checking_access == access_code:
                    self.users[username] = {"password":password,"role":"admin"}
                    self.save_user()
                    return f"Registration successful, you are now one of admins of the Society"
                else:
                    print("incorrect access code! Your role is going to be member")        
                    self.users[username] = {"password":password,"role":"member"}
                    self.save_user()
                    return f"Registration successful, you are now a member of the Society"
            elif admin_or_member.lower() == "member":
                self.users[username] = {"password":password,"role":"member"}
                self.save_user()
                return f"Registration successful, you are now a member of the Society"
            else:
                raise ValueError("You have to choose between member or admin!")
            
        
