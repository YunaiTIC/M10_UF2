import json

class Vehicle:
    def __init__(self, marca, model, any, color, quilometratge, preu):
        self.marca = marca
        self.model = model
        self.any = any
        self.color = color
        self.quilometratge = quilometratge
        self.preu = preu


    def obtenir_marca(self):
        return self.marca

    def obtenir_model(self):
        return self.model

    def obtenir_any(self):
        return self.any

    def obtenir_color(self):
        return self.color

    def obtenir_quilometratge(self):
        return self.quilometratge

    def obtenir_preu(self):
        return self.preu

    # Setters
    def establir_marca(self, marca):
        self.marca = marca

    def establir_model(self, model):
        self.model = model

    def establir_any(self, any):
        self.any = any

    def establir_color(self, color):
        self.color = color

    def establir_quilometratge(self, quilometratge):
        self.quilometratge = quilometratge

    def establir_preu(self, preu):
        self.preu = preu

    def mostrar_dades(self):
        print("Marca:", self.marca)
        print("Model:", self.model)
        print("Any:", self.any)
        print("Color:", self.color)
        print("Quilometratge:", self.quilometratge)
        print("Preu:", self.preu)

    def to_dict(self):
        return {
            "marca": self.marca,
            "model": self.model,
            "any": self.any,
            "color": self.color,
            "quilometratge": self.quilometratge,
            "preu": self.preu
        }


cotxe = Vehicle("Toyota", "Camry", 2022, "Blau", 15000, 25000)
cotxe.mostrar_dades()
print(json.dumps(cotxe.to_dict(), indent=4))
