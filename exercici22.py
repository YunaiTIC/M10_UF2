import xml.etree.ElementTree as ET

def crear_xml():
    arrel = ET.Element("students")


    for i in range(1, 6):
        estudiant = ET.SubElement(arrel, "student", attrib={"id": str(i)})


        nom = ET.SubElement(estudiant, "name")
        cognom = ET.SubElement(estudiant, "surname")
        email = ET.SubElement(estudiant, "email")
        dni = ET.SubElement(estudiant, "dni")


        nom.text = f"Nom{i}"
        cognom.text = f"Cognom{i}"
        email.text = f"email{i}@exemple.com"
        dni.text = f"DNI{i}"


    arbre = ET.ElementTree(arrel)
    arbre.write("estudiants.xml")

    with open("estudiants.xml", "r") as fitxer:
        contingut_xml = fitxer.read()
        print(contingut_xml)

crear_xml()
