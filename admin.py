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
    
def save_mission():
     with open(path,"w") as file:
            json.dump(missions,file,indent=2)


def create_mission(admin_username:str):
    title = input("Enter the mission title: ")
    description = input("Enter mission description: ")
    if description in missions_dict[title]:
        return "There is a mission like this that already exists!"
    else:
        missions_dict[title] = {"description":description}
        with open(path,"w") as file:
            json.dump(missions_dict,file,indent=2)
    return f"Mission create with ID: 00"
