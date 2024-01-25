from quadrat import calcular_quadrat
from aplicar_funcio import aplicar_funcio_a_llista


def main():
    llista_original = [1, 2, 3, 4, 5]
    print("Llista original:", llista_original)

    llista_nova = aplicar_funcio_a_llista(calcular_quadrat, llista_original)
    print("Llista nova amb quadrats:", llista_nova)


if __name__ == "__main__":
    main()
