from calcul import suma

def demanar_numeros():
    try:
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))
        return num1, num2
    except ValueError:
        print("Error: Has d'introduir dos números vàlids.")

def main():
    numeros = demanar_numeros()
    if numeros:
        resultat = suma(*numeros)
        print("La suma és:", resultat)

if __name__ == "__main__":
    main()
