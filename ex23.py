import json

json_data = [
    {
        "book": {
            "titol": "Pepito Conejo",
            "cover": "Conill",
            "year": 2012,
            "pages": 37
        }
    },
    {
        "book": {
            "titol": "El Màgic Món de les Fades",
            "cover": "Fada",
            "year": 2015,
            "pages": 48
        }
    },
    {
        "book": {
            "titol": "Aventures al Planeta Vermell",
            "cover": "Mars",
            "year": 2018,
            "pages": 56
        }
    },
    {
        "book": {
            "titol": "Viatge a les Profunditats de l'Oceà",
            "cover": "Oceà",
            "year": 2020,
            "pages": 42
        }
    }
]

def ex23():
    with open("llibres.json", "w") as json_file:
        json.dump(json_data, json_file, indent=2)

ex23()
