import os
import json

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
    data = load_missions()
    missions = data["missions"]
    for mission in missions:
        if description.strip().lower() == mission["description"].strip().lower():
            return f"A missions with this {description} already exist!"

    new_mission = {"id":len(missions)+1,"title":title,"description":description,"created_by":admin_username,"completed_by":[]}
    missions.append(new_mission)
    save_mission(data)
    return f"You create a mission successfully with ID: {new_mission["id"]}"
