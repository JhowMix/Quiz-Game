import json
import pathlib

root_path = pathlib.Path().parent.absolute()

def getData():
  with open(str(root_path)+'\data\data.json', 'r') as json_file:
    return json.load(json_file)