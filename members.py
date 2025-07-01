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

def view_available_missions(username:str):
    """This will show the user the available missions to him/her but only the missions that the user didn't complete"""
    data = load_missions()
    missions = data["missions"]
    available_missions = [mission for mission in missions if username not in mission["completed_by"]]
    if not available_missions:
        return "You completed all the avaliable missions 🎉"
    
    print("Avaliable missions:")
    for mission in available_missions:
        print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}]")

def submit_mission(username:str):
    """This function allow the user to enter the ID of the mission that he want to submit to complete"""
    data = load_missions()
    missions = data["missions"]
    if not missions:
        return Fore.RED + "There is no missions yet!"
    available_missions = [mission for mission in missions if username not in mission["completed_by"]]
    if not available_missions:
        return "There is no avaliable missions for you to solve 🎉"
    try:
        mission_id = int(input("Enter the ID of the mission that you want to submit: "))
    except ValueError:
         return "Invalid ID"
    for mission in missions:
        if mission["id"] == mission_id:
            if username not in mission["completed_by"]:
                answer = input("Enter the answer for this mission: ").strip().lower()
                if mission["answer"] == answer:
                    mission["completed_by"].append(username)
                    users = auth._users
                    users[username]["missions_completed"] += 1
                    completed = users[username]["missions_completed"]
                    if completed >= 10:
                        users[username]["rank"] = "Mastermind"
                    elif completed >= 5:
                        users[username]["rank"] = "Solver"
                    elif completed >= 3:
                        users[username]["rank"] = "Explorer"
                    else:
                        users[username]["rank"] = "Novice"
                    auth.save_user()
                    save_mission(data)
                    return Fore.GREEN +"👏 Congratulations you completed the mission, Now the mission is marked as completed "
                else:
                    return Fore.RED + "[❌] Wrong answer!"
            else:
                return Fore.RED +  f"[❌] You already done from this mission with this ID {mission["id"]}!"
    return Fore.RED + "[❌] There is no mission with this ID"


def view_progress(username:str):
    """This will show the user his/her rank and the number of missions that he completed also will view what mission he/she completed"""
    users = auth._users
    data = load_missions()
    missions = data["missions"]
    print(f"Agent {username} \n  rank: {users[username]["rank"]} \n  number of completed missions: {users[username]["missions_completed"]}")
    completed_missions = [mission for mission in missions if username in mission["completed_by"]]
    if not completed_missions:
        print("You didn't complete any mission yet!")
    else:
        print("The missions you completed:")
        for mission in completed_missions:
            print(Fore.GREEN + f"    {mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}]")
         
    



         

    