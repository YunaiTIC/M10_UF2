
l=[]
w1 = input("Dime una palabra")
l.append(w1)
z = input("Quieres añadir otra (y/n) ")
if z == "y":
    w2 = input("Dime una palabra")
    l.append(w2)
    z = input("Quieres añadir otra (y/n) ")
    if z == "y":
        w3 = input("Dime una palabra")
        l.append(w3)

for x in l:
    print(len(x))
    print(x[0])
    print(x[1])
    print("\n")
