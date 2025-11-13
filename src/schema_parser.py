import json

def load_schema(file_path):
    with open(file_path, "r") as f:
        schema = json.load(f)
    return schema

def load_stats(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
