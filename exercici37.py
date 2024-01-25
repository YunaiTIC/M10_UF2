def amb_iva(ftotal, iva=21):
    ftotal = float(ftotal)
    ftotal_amb_iva = ftotal * (1 + iva / 100)
    return ftotal_amb_iva


ftotal = input('Introdueix el preu de tot el carrito: ')
print(amb_iva(ftotal))
