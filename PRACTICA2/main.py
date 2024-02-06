from create import create_record
from read import read_records
from update import update_record
from delete import delete_record

def main_menu():
    print("Benvingut al menú principal:")
    print("1. Crear un nou registre")
    print("2. Llegir tots els registres")
    print("3. Actualitzar un registre")
    print("4. Esborrar un registre")
    print("5. Sortir")

def main():
    while True:
        main_menu()
        choice = input("Selecciona una opció (1-5): ")

        if choice == "1":
            create_record()
        elif choice == "2":
            read_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            print("Gràcies per utilitzar el programa. Adeu!")
            break
        else:
            print("Opció invàlida. Si us plau, selecciona una opció vàlida.")

main()
