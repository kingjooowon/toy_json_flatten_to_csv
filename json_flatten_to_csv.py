import json
import csv

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def flatten_to_rows(data, path="", rows=None):
    if rows is None:
        rows = [{}]
    
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            dict_rows = flatten_to_rows(value, new_path, rows)
            rows = dict_rows
    
    elif isinstance(data, list):
        new_rows = []
        for row in rows:
            for item in data:
                copied = row.copy()
                temp_rows = flatten_to_rows(item, path, [copied])
                new_rows.extend(temp_rows)
        rows = new_rows
        
    else:
        for row in rows:
            row[path] = data
        
    return rows

def write_csv(rows, out_path):
    if not rows:
        return
    
    headers = rows[0].keys()
    
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
    
if __name__ == "__main__":
    data = read_json("sample.json")
    rows = flatten_to_rows(data)
    write_csv(rows, "ouput.csv")
    print(rows)