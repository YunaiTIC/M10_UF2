import psycopg2
from connection import get_connection

def read_records():
    conn = get_connection()  # Obtenir una connexió a la base de dades
    cur = conn.cursor()  # Crear un objecte cursor per executar consultes SQL

    try:
        cur.execute("SELECT * FROM Videojocs;")  # Executar una consulta SELECT
        rows = cur.fetchall()  # Recuperar totes les files resultants
        for row in rows:
            print(row)  # Imprimir cada fila
    except psycopg2.Error as e:
        print("Error en llegir els registres:", e)  # Capturar i imprimir errors
    finally:
        cur.close()  # Tancar l'objecte cursor
        conn.close()  # Tancar la connexió a la base de dades

read_records()
