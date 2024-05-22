from robot.libraries.BuiltIn import BuiltIn
import json

def convert_to_json(number, text):
    data = {"top": str(number), "tt": text}
    return json.dumps(data, ensure_ascii=False)
