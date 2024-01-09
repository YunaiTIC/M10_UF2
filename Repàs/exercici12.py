meses_del_año = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

x = int(input("Numero 0-12 "))

while x != 0:
    print(meses_del_año[x-1])
    x = int(input("Numero 0-12 "))