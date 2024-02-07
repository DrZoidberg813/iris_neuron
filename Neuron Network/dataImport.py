import json
import random
import re

def dataImport(data_loc: str, _bool: bool) -> None:
    
    if _bool == False:
        return 
    
    with open(data_loc, "r") as f:
        data = f.readlines()
        f.close
        
    random.shuffle(data)
        
    data_dict = {}
        
    for i, item in enumerate(data):
        splt = re.split(",|\n", item)
            
        data_dict[f"{splt[4]}, {i}"] = {
            "Sepal length": float(splt[0]),
            "Sepal weidth": float(splt[1]),
            "Petal length": float(splt[2]),
            "Petal weidth": float(splt[3])
            }
        
    with open("data_list.json", "w", encoding="utf-8-sig") as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)
        f.close