from random_number import generar_numero_aleatori

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
        aleatori = generar_numero_aleatori(num1, num2)
        print("El número aleatori entre", num1, "i", num2, "és:", aleatori)

if __name__ == "__main__":
    main()
