x=int(input("DIgue'm preu en € "))
y = int(input("% d'IVA a aplicar "))

res = y * x / 100
print("Has indicat " + str(x) + " amb un iva de " + str(y))
print("El preu final es " + str(x+res))

