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
