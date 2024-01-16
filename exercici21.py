
numeros_usuario = input("Introdueix 10 números separats per espais: ")
lista_numeros = [float(num) for num in numeros_usuario.split()]


suma_total = sum(lista_numeros)
mitjana = suma_total / len(lista_numeros)


lista_numeros.append(suma_total)
lista_numeros.append(mitjana)

print("\nNúmeros de l'usuari:")
print(lista_numeros)
print("Suma total:", suma_total)
print("Mitjana:", mitjana)
