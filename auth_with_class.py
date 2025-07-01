import json
import os
from colorama import init, Fore
init(autoreset=True)


class Auth:
    def __init__(self):
        self._path = "D:/Units/UNIT-PROJECT-1/data/users.json"
        self._path_rejected_users = "D:/Units/UNIT-PROJECT-1/data/rejected_users.json"
        self._users = self.load_user()
        self._rejected_users = self.load_rejected_user()
        self.__access_code = "@superaccess123" #this one is only needed when someone want to register as admin
    def load_user(self):
        """it will load the users in users.json"""
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
        """it will save the users in users.json"""
        with open(self._path,"w") as file:
            json.dump(self._users,file,indent=2)
    def load_rejected_user(self):
        """it will load the rejected_users in rejected_users.json"""
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
        """This function is going to take the users that the admin reject and save them in rejected_users.json"""
        self._rejected_users.update(user)
        with open(self._path_rejected_users,"w") as file:
            json.dump(self._rejected_users,file,indent=2)
    
    def login(self,username,password):
        """This function is going to take the username and password to check and login in if can"""
        if username in self._users:
            if self._users[username]["password"] == password:
                if self._users[username]["role"] == "admin":
                    return {"username":username,"role":"admin"}
                else:
                    return {"username":username,"role":"member","approval_status":self._users[username]["approval_status"]}
            else:
                raise ValueError(Fore.RED + "[❌] incorrect password!")
        elif username in self._rejected_users:
            if self._rejected_users[username]["password"] == password:
                raise ValueError(Fore.RED + f"You have been rejected! You can't login with this username: {username}")
            else:
                raise ValueError(Fore.RED + "[❌] incorrect password!")
        else:
            raise ValueError(Fore.RED + "[❌] The username doesn't exist!")
        
    def register(self,username,password):
        """This function is for both admin and member but to became an admin you need to have the access code
        and if you didn't get it right you will become a member auto"""
        if not username:
            raise ValueError(Fore.RED + "You need to enter a username!")
        if not password:
            raise ValueError(Fore.RED + "You need to enter a password!")
        if username[0].isdigit():
            raise ValueError(Fore.RED + "Username can't start with a digit!")
        if len(password) < 8:
            raise ValueError(Fore.RED + "The length of the password can't be less than 8!")
        if username in self._users:
            raise ValueError(Fore.RED + "The username already exists!")
        if username in self._rejected_users and self._rejected_users[username]["password"] == password:
            raise ValueError(Fore.RED + f"This username: {username} is rejected!")
        else:
            
            admin_or_member = input("Do you want to register as admin or member? ")
            if admin_or_member.lower() == "admin":
                checking_access = input("Enter admin access code: ")
                if checking_access == self.__access_code:
                    self._users[username] = {"password":password,"role":"admin"}
                    self.save_user() 
                    print(Fore.GREEN + "[✔] Registration successful, you are now one of admins of the Society")
                    return {"username":username,"role":"admin"}
                else:
                    print(Fore.RED + "[❌] incorrect access code! Your role is going to be member")
                    reason = input("Why should the Society accept you? (State your reason in one sentence): ")        
                    self._users[username] = {"password":password,"role":"member","rank":"Novice","missions_completed": 0, "approval_status":False,"reason":reason}
                    self.save_user() 
                    print(Fore.GREEN + f"[✔] Registration successful")
                    return {"username":username,"role":"member"}
            elif admin_or_member.lower() == "member":
                member_reason = input("Why should the Society accept you? (State your reason in one sentence): ")  
                self._users[username] = {"password":password,"role":"member","rank":"Novice","missions_completed": 0, "approval_status":False,"reason":member_reason}
                self.save_user()
                print(Fore.GREEN + f"[✔] Registration successful")
                return {"username":username,"role":"member"}
            else:
                raise ValueError(Fore.RED + "You have to choose between member or admin!")
            
        
    def view_all_users(self):
        """It will view all users with their roles"""
        for username , details in self._users.items():
            print(f"{username} - Role: {details["role"]}")
    
    def promote_to_admin(self,username:str):
        """This function will allow the admin to promote a member to become a admin"""
        if username not in self._users:
            return Fore.RED + f"[❌] This username: {username} doesn't exist!"
        elif self._users[username]["role"] == "admin":
            return Fore.RED + f"[❌] This username: {username} is already an admin!"
        else:
            self._users[username]["role"] = "admin"
            self.save_user()
            return Fore.GREEN + f"{username} has been promoted to admin [✔]"
        