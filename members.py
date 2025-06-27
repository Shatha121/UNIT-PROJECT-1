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

def view_available_missions(username:str):
    data = load_missions()
    missions = data["missions"]
    avaliable_missions = [mission for mission in missions if username not in mission["completed_by"]]
    if not avaliable_missions:
        return "You completed all the avaliable missions 🎉"
    
    print("Avaliable missions:")
    for mission in avaliable_missions:
        print(f"{mission["id"]}. Title: {mission["title"]} [Description -> {mission["description"]}]")

         

    