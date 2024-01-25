from numbers import mostrar_nums_entre

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
        num1, num2 = numeros
        mostrar_nums_entre(num1, num2)

if __name__ == "__main__":
    main()
