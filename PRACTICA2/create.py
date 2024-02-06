import psycopg2
from connection import get_connection

def create_record():
    conn = get_connection()  # Obtenir una connexió a la base de dades
    cur = conn.cursor()  # Crear un objecte cursor per executar consultes SQL

    try:
        cur.execute("""
            INSERT INTO Videojocs (nom, descripcio, categoria, autor, preu, data_sortida)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, ("nom_joc", "descripcio_joc", "categoria_joc", "autor_joc", 59.99, "2024-01-01"))
        conn.commit()  # Confirmar els canvis a la base de dades
        print("Registre creat amb èxit.")  # Imprimir missatge de confirmació
    except psycopg2.Error as e:
        print("Error en crear el registre:", e)  # Capturar i imprimir errors
    finally:
        cur.close()  # Tancar l'objecte cursor
        conn.close()  # Tancar la connexió a la base de dades

create_record()
