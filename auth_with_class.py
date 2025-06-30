import json
import os

class Auth:
    def __init__(self):
        self._path = "D:/Units/UNIT-PROJECT-1/data/users.json"
        self._path_rejected_users = "D:/Units/UNIT-PROJECT-1/data/rejected_users.json"
        self._users = self.load_user()
        self._rejected_users = self.load_rejected_user()
        self.__access_code = "@superaccess123"
    def load_user(self):
        if os.path.exists(self._path):
            with open(self._path,"r") as file:
                try:
                    users_dict = json.load(file)
                except json.JSONDecodeError:
                    users_dict = {}
        else:
            users_dict = {}
        return users_dict
    def save_user(self):
        with open(self._path,"w") as file:
            json.dump(self._users,file,indent=2)
    def load_rejected_user(self):
        if os.path.exists(self._path_rejected_users):
            with open(self._path_rejected_users,"r") as file:
                try:
                    users_rejected_users_dict = json.load(file)
                except json.JSONDecodeError:
                    users_rejected_users_dict = {}
        else:
            users_rejected_users_dict = {}
        return users_rejected_users_dict
    def save_rejected_user(self,user):
        self._rejected_users.update(user)
        with open(self._path_rejected_users,"w") as file:
            json.dump(self._rejected_users,file,indent=2)
    
    def login(self,username,password):
        if username in self._users:
            if self._users[username]["password"] == password:
                if self._users[username]["role"] == "admin":
                    return {"username":username,"role":"admin"}
                else:
                    return {"username":username,"role":"member","approval_status":self._users[username]["approval_status"]}
            else:
                raise ValueError("incorrect password!")
        elif username in self._rejected_users:
            if self._rejected_users[username]["password"] == password:
                raise ValueError(f"You have been rejected! You can't login with this username: {username}")
            else:
                raise ValueError("incorrect password!")
        else:
            raise ValueError("The username doesn't exist!")
        
    def register(self,username,password):
        if not username:
            raise ValueError("You need to enter a username!")
        if not password:
            raise ValueError("You need to enter a password!")
        if username[0].isdigit():
            raise ValueError("Username can't start with a digit!")
        if username in self._users:
            raise ValueError("The username already exists!")
        if username in self._rejected_users and self._rejected_users[username]["password"] == password:
            raise ValueError("This username is rejected!")
        else:
            
            admin_or_member = input("Do you want to register as admin or member? ")
            if admin_or_member.lower() == "admin":
                checking_access = input("Enter admin access code: ")
                if checking_access == self.__access_code:
                    self._users[username] = {"password":password,"role":"admin"}
                    self.save_user() 
                    print("Registration successful, you are now one of admins of the Society")
                    return {"username":username,"role":"admin"}
                else:
                    print("incorrect access code! Your role is going to be member")        
                    self._users[username] = {"password":password,"role":"member","rank":"Novice","missions_completed": 0, "approval_status":False}
                    self.save_user() 
                    print(f"Registration successful")
                    return {"username":username,"role":"member"}
            elif admin_or_member.lower() == "member":
                self._users[username] = {"password":password,"role":"member","rank":"Novice","missions_completed": 0, "approval_status":False}
                self.save_user()
                print(f"Registration successful")
                return {"username":username,"role":"member"}
            else:
                raise ValueError("You have to choose between member or admin!")
            
        
    def view_all_users(self):
        for username , details in self._users.items():
            print(f"{username} - Role: {details["role"]}")
    
    def promote_to_admin(self,username:str):
        if username not in self._users:
            return f"This username: {username} doesn't exist!"
        elif self._users[username]["role"] == "admin":
            return f"This username: {username} is already an admin!"
        else:
            self._users[username]["role"] = "admin"
            self.save_user()
            return f"{username} has been promoted to admin"
        