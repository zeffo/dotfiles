import json

with open("config", "r+") as f:
    data = json.load(f)
    f.seek(0)
    json.dump(data, f, indent=4)
