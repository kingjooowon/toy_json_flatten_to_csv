import json
import csv

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def flatten_to_rows(data, path=""):
    rows = [{}]
    
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            flatten_to_rows(value, new_path)
    
    elif isinstance(data, list):
        new_rows = []
        for row in rows:
            for item in data:
                copied = row.copy()
                copied[path] = item
                new_rows.append(copied)
        rows = new_rows
        
    else:
        rows.append(data)
        
    return rows