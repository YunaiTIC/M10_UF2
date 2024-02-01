import psycopg2
from connection import get_connection

def create_record():
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO Videojocs (nom, descripcio, categoria, autor, preu, data_sortida)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, ("FFVII", "Nou remake del final fantasy", "JRPG", "Hironobu Sakaguchi", 69.99, "2024-01-01"))
        conn.commit()
        print("Registre creat amb èxit.")
    except psycopg2.Error as e:
        print("Error en crear el registre:", e)
    finally:
        cur.close()
        conn.close()

create_record()
