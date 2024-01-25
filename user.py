import json

class User:
    def __init__(self, nom, cognom, edat, ciutat, email, telefon):
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.ciutat = ciutat
        self.email = email
        self.telefon = telefon

    def obtenir_nom(self):
        return self.nom

    def obtenir_cognom(self):
        return self.cognom

    def obtenir_edat(self):
        return self.edat

    def obtenir_ciutat(self):
        return self.ciutat

    def obtenir_email(self):
        return self.email

    def obtenir_telefon(self):
        return self.telefon


    def establir_nom(self, nom):
        self.nom = nom

    def establir_cognom(self, cognom):
        self.cognom = cognom

    def establir_edat(self, edat):
        self.edat = edat

    def establir_ciutat(self, ciutat):
        self.ciutat = ciutat

    def establir_email(self, email):
        self.email = email

    def establir_telefon(self, telefon):
        self.telefon = telefon

    def salutacio(self):
        print("Nom:", self.nom)
        print("Cognom:", self.cognom)
        print("Edat:", self.edat)
        print("Ciutat:", self.ciutat)
        print("Email:", self.email)
        print("Telefon:", self.telefon)

    def to_dict(self):
        return {
            "nom": self.nom,
            "cognom": self.cognom,
            "edat": self.edat,
            "ciutat": self.ciutat,
            "email": self.email,
            "telefon": self.telefon
        }


usuari = User("Joan", "Martínez", 30, "Barcelona", "joan@gmail.com", "123456789")
usuari.salutacio()
print(json.dumps(usuari.to_dict(), indent=4))
