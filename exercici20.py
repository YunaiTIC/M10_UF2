agenda = {}

while True:
    nom = input("Introdueix el nom del contacte (o 'stop' per finalitzar): ")

    if nom.lower() == 'stop':
        break

    edat = input("Introdueix l'edat del contacte: ")

    if nom in agenda:
        print(f"Aquest nom ja està a l'agenda. No s'afegirà duplicat.")
    else:
        agenda[nom] = int(edat)

print("\nAgenda final:")
for nom, edat in agenda.items():
    print(f"{nom}: {edat} anys")
