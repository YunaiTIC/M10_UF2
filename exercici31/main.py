from invoice import calcular_total_factura

def demanar_dades_factura():
    try:
        quantitat_sense_iva = float(input("Introdueix la quantitat sense IVA: "))
        iva = int(input("Introdueix l'IVA a aplicar (4%, 10% o 21%): "))
        return quantitat_sense_iva, iva
    except ValueError:
        print("Error: Has d'introduir un valor numèric.")

def main():
    quantitat_sense_iva, iva = demanar_dades_factura()
    calcular_total_factura(quantitat_sense_iva, iva)

if __name__ == "__main__":
    main()
