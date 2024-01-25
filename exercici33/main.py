from compra import calcular_total_compra

def demanar_iva():
    try:
        iva = float(input("Introdueix l'IVA a aplicar (en percentatge): "))
        return iva
    except ValueError:
        print("Error: Has d'introduir un valor numèric.")

def main():
    llista_compra = {100: 10, 250: 5, 1500: 30}
    iva = demanar_iva()
    if iva is not None:
        calcular_total_compra(llista_compra, iva)

if __name__ == "__main__":
    main()
