from auth_with_class import Auth
from admin import create_mission,view_missions,review_submitted_missions,accept_pending_users
from members import view_available_missions, submit_missions,view_progress


auth = Auth()

def admin_menu(user:dict):
    print(f"Welcome Admin {user['username']}, What would you like to do?")
    while True:
        admin_choice = input("1)View All Users \n2)Promote User \n3)View Missions \n4)Create Mission \n5)review submitted missions \n6)accept pending users \n7)Logout \nChoice: ")
        if admin_choice == "1":
            print()
            print("-"*15)
            auth.view_all_users()
            print("-"*15)
        elif admin_choice == "2":
            print()
            print("-"*15)
            member_name = input("Enter the username of the member that you want to promote to admin: ")
            print(auth.promote_to_admin(member_name))
            print("-"*15)
        elif admin_choice == "3":
            print()
            print("-"*15)
            view_missions()
            print("-"*15)
        elif admin_choice == "4":
            print()
            print("-"*15)
            print(create_mission(user))
            print("-"*15)
        elif admin_choice == "5":
            print()
            print("-"*15)
            review_submitted_missions()
            print("-"*15)
        elif admin_choice == "6":
            print()
            print("-"*15)
            accept_pending_users()
            print("-"*15)
        elif admin_choice == "7" or admin_choice.lower() == "logout":
            print()
            print("-"*15)
            print("Bye👋")
            print("-"*15)
            break
        else:
            print("Wrong! You can choose from 1 to 6")




def member_menu(user:dict):
    print(f"Welcome {user['username']}, What would you like to do?")
    while True:
        member_choice = input("1)View Missions \n2)Submit Mission Report \n3)View progress \n4)Logout \nChoice: ")
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
        elif member_choice == "3":
            print()
            print("-"*15)
            view_progress(user["username"])
            print("-"*15)
        elif member_choice == "4" or member_choice.lower() == "logout":
            print("Bye👋")
            break
        else:
            print("Wrong! You can choose from 1 to 4")



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
            print("Your account is pending. Please wait until your registration approved before logging in")
        break
    elif register_or_login.lower() == 'login':
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        user = auth.login(username,password)
        if user["role"] == "admin":
            admin_menu(user)
        else:
            if user["approval_status"] == True:
                member_menu(user)
            else:
                print("Your account is still pending admin approval. Please wait until your registration approved before logging in")
        break
    else:
        print("You need to choose either register or login")
