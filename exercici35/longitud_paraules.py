def calcular_longitud_paraules(frase):
    paraules = frase.split()
    longitud_paraules = {paraula: len(paraula) for paraula in paraules}
    return longitud_paraules
