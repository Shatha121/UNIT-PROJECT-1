import os
import json
from auth_with_class import Auth

auth = Auth()


path = "D:/Units/UNIT-PROJECT-1/data/missions.json"

def load_missions():
    if os.path.exists(path):
        with open(path,"r") as file:
            try:
                    return json.load(file)
            except json.JSONDecodeError:
                    return {"missions":[]}
    else:
        return {"missions":[]}
    
def save_mission(data):
     with open(path,"w") as file:
            json.dump(data,file,indent=2)



def create_mission(admin_username:str):
    title = input("Enter the mission title: ")
    description = input("Enter mission description: ")
    answer = input("Enter the answer for the mission: ")
    data = load_missions()
    missions = data["missions"]
    for mission in missions:
        if description.strip().lower() == mission["description"].strip().lower():
            return f"A missions with this {description} already exist!"

    new_mission = {"id":len(missions)+1,"title":title,"description":description,"created_by":admin_username,"answer":answer.strip().lower(),"completed_by":[]}
    missions.append(new_mission)
    save_mission(data)
    return f"You create a mission successfully with ID: {new_mission["id"]}"

#just to see all the missions. without caring if it completed by someone or not
def view_missions():
    if not os.path.exists(path):
        print("missions.json file not found")
        return
    data = load_missions()
    missions = data["missions"]
    for mission in missions:
        if mission["completed_by"] == []:
            print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}, Created by: {mission["created_by"]["username"]}, Answer for the mission: {mission["answer"]} ,Solved by members: None]")
        else:
            print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}, Created by: {mission["created_by"]["username"]}, Answer for the mission: {mission["answer"]} , Solved by members: {mission["completed_by"]}]")


def review_submitted_missions():
    if not os.path.exists(path):
        print("missions.json file not found")
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
    users = auth.users
    users_to_delete = []
    member_to_approve = False
    for username, datails in users.items():
        if datails["role"] == "member":
            if datails["approval_status"] == False:
                member_to_approve = True
                print(f"{username}")
                admin_choise =input("Do you approve this member joining ? type 'y' for yes or type 'n' for no: ")
                if admin_choise == "y":
                    users[username]["approval_status"] = True
                    auth.save_user()
                    print(f"You have accepted {username}")
                elif admin_choise == "n":
                    user = {username:datails}
                    auth.save_rejected_user(user)
                    users_to_delete.append(username)
                    print(f"You have rejected {username}")
                else:
                    print("You need to type either 'y' or 'n' !")    
        else:
            continue
    if member_to_approve == False:
        print("There isn't any member left to approve!")
    for user in users_to_delete:
        del users[user]        
        auth.save_user()
