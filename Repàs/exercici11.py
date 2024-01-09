list=[]

x = int(input("Num del 10 al 100"))

z = 1
for z in range(x+1):
    list.append(z)

z = tuple(list)

print(z)
