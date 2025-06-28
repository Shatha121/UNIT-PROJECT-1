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

def view_available_missions(username:str):
    data = load_missions()
    missions = data["missions"]
    avaliable_missions = [mission for mission in missions if username not in mission["completed_by"]]
    if not avaliable_missions:
        return "You completed all the avaliable missions 🎉"
    
    print("Avaliable missions:")
    for mission in avaliable_missions:
        print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}]")

def submit_missions(username:str):
    data = load_missions()
    missions = data["missions"]
    avaliable_missions = [mission for mission in missions if username not in mission["completed_by"]]
    if not avaliable_missions:
        return "There is no avaliable missions for you to solve 🎉"
    try:
        mission_id = int(input("Enter the ID of the mission that you want to submit: "))
    except ValueError:
         return "Invalid ID"
    for mission in missions:
        if mission["id"] == mission_id:
            answer = input("Enter the answer for this mission: ").strip().lower()
            if mission["answer"] == answer:
                mission["completed_by"].append(username)
                users = auth.users
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
                return "👏 Congratulations you completed the mission, Now the mission is marked as completed "
            else:
                return "Wrong answer!"
    return "There is no mission with this ID"


         

    