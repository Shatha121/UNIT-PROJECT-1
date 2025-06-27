from auth_with_class import Auth
from admin import create_mission,view_missions
from members import view_available_missions, submit_missions

def admin_menu(user:dict):
    print(f"Welcome Admin {user['username']}, What would you like to do?")
    while True:
        admin_choice = input("1)View All Users \n2)Promote User \n3)View Missions \n4)Create Mission \n5)Logout \nChoice:")
        if admin_choice == "1":
            pass
        elif admin_choice == "2":
            pass
        elif admin_choice == "3":
            view_missions()
        elif admin_choice == "4":
            print(create_mission(user))
        elif admin_choice == "5" or admin_choice.lower() == "logout":
            print("Bye👋")
            break
        else:
            print("Wrong! You can choose from 1 to 5")




def member_menu(user:dict):
    print(f"Welcome {user['username']}, What would you like to do?")
    while True:
        member_choice = input("1)View Missions \n2)Submit Mission Report \n3)Logout \nChoice: ")
        if member_choice == "1":
            print()
            print("-"*15)
            view_available_missions(user["username"])
            print("-"*15)
        elif member_choice == "2":
            print()
            print("-"*15)
            print(submit_missions(user["username"]))
            print("-"*15)
        elif member_choice == "3" or member_choice.lower() == "logout":
            print("Bye👋")
            break
        else:
            print("Wrong! You can choose from 1 to 3")


auth = Auth()
while True:
    register_or_login = input("Type 'register' or 'login' and if you want to leave type exit: ")
    if register_or_login.lower() == 'exit':
        print("Bye")
        break
    if register_or_login.lower() == 'register':
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        user = auth.register(username,password)
        if user["role"] == "admin":
            admin_menu(user)
        else:
            member_menu(user)
        break
    elif register_or_login.lower() == 'login':
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        user = auth.login(username,password)
        if user["role"] == "admin":
            admin_menu(user)
        else:
            member_menu(user)
        break
    else:
        print("You need to choose either register or login")
