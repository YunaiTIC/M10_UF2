
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

tupla_paraules = (paraula1, paraula2)

comptador_ocurr = {}

for paraula in tupla_paraules:
    for lletra in paraula:
        if lletra in comptador_ocurr:
            comptador_ocurr[lletra] += 1
        else:
            comptador_ocurr[lletra] = 1

print("Quantitat d'aparicions de cada lletra:")
for lletra, comptador in comptador_ocurr.items():
    print(f"{lletra}: {comptador}")
