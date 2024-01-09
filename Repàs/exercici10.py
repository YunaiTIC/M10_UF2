import random

x = random.randint(1,100)
print(x)
g = 101
contadorveces = 0

while g!=x:
    contadorveces += 1
    g = int(input("Digues el num: "))
    if g<x:
        print("Es més gran. Prova una altra vegada ")
    elif g>x:
        print("Es més petit. Prova una altra vegada ")

print("Enhorabona, has encertat el num en " + str(contadorveces) + " vegades")


