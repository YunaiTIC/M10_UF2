def calcular_total_compra(llista_compra, iva):
    total_descomptat = 0

    print("Llista de la compra amb descompte aplicat i IVA:")
    for index, (preu, descompte) in enumerate(llista_compra.items(), start=1):
        preu_descomptat = preu - (preu * descompte / 100)
        total_descomptat += preu_descomptat
        total_amb_iva = preu_descomptat * (1 + iva / 100)
        print(f"Producte {index}: {total_amb_iva:.2f} €")

    print(f"\nTotal de la compra amb descompte aplicat i IVA: {total_descomptat * (1 + iva / 100):.2f} €")
