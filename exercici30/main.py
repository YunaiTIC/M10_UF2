from greeting import saludar

def demanar_nom():
    nom = input("Introdueix el teu nom: ")
    return nom

def main():
    nom = demanar_nom()
    saludar(nom)

if __name__ == "__main__":
    main()
