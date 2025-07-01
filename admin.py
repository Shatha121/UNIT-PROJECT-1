import os
import json
from auth_with_class import Auth
from colorama import init, Fore
init(autoreset=True)

auth = Auth()


path = "D:/Units/UNIT-PROJECT-1/data/missions.json"

def load_missions():
    """it will load the missions into missions.json"""
    if os.path.exists(path):
        with open(path,"r") as file:
            try:
                    return json.load(file)
            except json.JSONDecodeError:
                    return {"missions":[]}
    else:
        return {"missions":[]}
    
def save_mission(data):
    """it will save the missions into missions.json"""
    with open(path,"w") as file:
            json.dump(data,file,indent=2)



def create_mission(admin_username:str):
    """This function will create missions with title , decription and answer"""
    title = input("Enter the mission title: ")
    if title == "":
        return Fore.RED +f"[❌] You need to enter a title!"
    description = input("Enter mission description: ")
    if description == "":
        return Fore.RED +f"[❌] You need to enter a description!"
    answer = input("Enter the answer for the mission: ")
    if answer == "":
        return Fore.RED +f"[❌] You need to enter an answer for the mission!"
    
    data = load_missions()
    missions = data["missions"]
    for mission in missions:
        if description.strip().lower() == mission["description"].strip().lower():
            return Fore.RED +f"[❌] A missions with this {description} already exist!"

    new_mission = {"id":len(missions)+1,"title":title,"description":description,"created_by":admin_username,"answer":answer.strip().lower(),"completed_by":[]}
    missions.append(new_mission)
    save_mission(data)
    return Fore.GREEN +f"[✔] You create a mission successfully with ID: {new_mission["id"]}"


def view_missions():
    """just to see all the missions. without caring if it completed by someone or not"""
    if not os.path.exists(path):
        print(Fore.RED +"[❌] missions.json file not found")
        return
    data = load_missions()
    missions = data["missions"]
    if not missions:
        print(Fore.RED+"There is no missions yet!")
    for mission in missions:
        if mission["completed_by"] == []:
            print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}, Created by: {mission["created_by"]["username"]}, Answer for the mission: {mission["answer"]} ,Solved by members: None]")
        else:
            print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}, Created by: {mission["created_by"]["username"]}, Answer for the mission: {mission["answer"]} , Solved by members: {mission["completed_by"]}]")


def review_submitted_missions():
    """This function will print the mission that is completed by memebers only"""
    if not os.path.exists(path):
        print(Fore.RED +"[❌] missions.json file not found")
        return
    data = load_missions()
    missions = data["missions"]
    any_completed = False
    for mission in missions:
        if mission["completed_by"]:
            any_completed = True
            print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}]")
            for member in mission["completed_by"]:
                print(f"    Solved by member: {member}")
            print()
    if not any_completed:
        print("No mission is completed yet!")


def accept_pending_users():
    """With this function the admin can accept or reject or skip the users"""
    users = auth._users
    users_to_delete = []
    member_to_approve = False
    for username, datails in users.items():
        if datails["role"] == "member":
            if datails["approval_status"] == False:
                member_to_approve = True
                print(f"{username}")
                print(f"Reason: {datails["reason"]}")
                admin_choise =input("Do you approve this member joining ? type 'y' for yes or type 'n' for no or type 's' if you are not sure: ")
                while True:
                    if admin_choise.lower() == "y":
                        users[username]["approval_status"] = True
                        auth.save_user()
                        print(Fore.GREEN + f"[✔] You have accepted {username}")
                        break
                    elif admin_choise.lower() == "n":
                        auth.save_rejected_user({username:datails})
                        users_to_delete.append(username)
                        print(Fore.YELLOW + f"[✔] You have rejected {username}")
                        break
                    elif admin_choise.lower() == "s":
                        break
                    else:
                        print(Fore.RED +"[❌] You need to type either 'y' or 'n' or 's'!")
                        print(f"{username}")
                        print(f"Reason: {datails["reason"]}")
                        admin_choise =input("Do you approve this member joining ? type 'y' for yes or type 'n' for no or type 's' if you are not sure: ")    
        else:
            continue
    if member_to_approve == False:
        print(Fore.RED +"There isn't any member left to approve!")
    for user in users_to_delete:
        del users[user]        
        auth.save_user()
