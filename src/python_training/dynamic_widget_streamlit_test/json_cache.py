import json

def result_serialize(obj: dict):
    with open('cache.json', 'w') as f:
        json.dump(obj, f)

def read_json():
    with open('cache.json', 'r') as f:
        updated_kv = json.load(f)
    
    return updated_kv