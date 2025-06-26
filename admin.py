import os
import json

path = "D:/Units/UNIT-PROJECT-1/data/missions.json"

if os.path.exists(path):
    with open(path,"r") as file:
        try:
                missions_dict = json.load(file)
        except json.JSONDecodeError:
                missions_dict = {}
else:
    missions_dict = {}


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
