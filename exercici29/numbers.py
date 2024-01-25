def mostrar_nums_entre(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    suma = 0
    print("Números entre", num1, "i", num2, ":")

    for i in range(int(num1) + 1, int(num2)):
        print(i)
        suma += i

    print("La suma dels números és:", suma)
