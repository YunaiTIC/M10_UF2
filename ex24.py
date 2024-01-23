import json
import os 

def llegirjson(file_path):
    with open(file_path, "r") as json_file:
        dades = json.load(json_file)
    return dades

def imprimirconsola(data):
    json_str = json.dumps(data)
    print(json_str)

def main():

    directoriscript = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directoriscript, "llibres.json")

    json_data = llegirjson(path)
    imprimirconsola(json_data)

main()
