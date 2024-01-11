f = input("Dime una frase ")

z =f.replace(" ", "")


chars={}

for x in z:
    if x not in chars:
        chars[x]=1
    else:
        chars[x]+=1

duplicates=[]
nonduplicates=[]

for x,y in chars.items():
    if y >1:
        duplicates.append(x)
    elif y ==1:
        nonduplicates.append(x)

tupla =tuple(nonduplicates)

print(tupla)