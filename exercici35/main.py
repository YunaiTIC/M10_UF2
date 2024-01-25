from longitud_paraules import calcular_longitud_paraules

def demanar_frase():
    frase = input("Introdueix una frase: ")
    return frase

def main():
    frase = demanar_frase()
    resultat = calcular_longitud_paraules(frase)
    print("Diccionari amb les paraules i la seva longitud:", resultat)

if __name__ == "__main__":
    main()
