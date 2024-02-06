import psycopg2
from connection import get_connection

def create_table():
    conn = get_connection()  # Obtenir una connexió a la base de dades
    cur = conn.cursor()  # Crear un objecte cursor per executar consultes SQL

    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Videojocs (
                nom varchar,
                descripcio varchar,
                categoria varchar,
                autor varchar,
                preu float,
                data_sortida date
            );
        """)  # Crear la taula Videojocs amb els camps especificats
        conn.commit()  # Confirmar els canvis a la base de dades
        print("Taula creada amb èxit.")  # Imprimir missatge de confirmació
    except psycopg2.Error as e:
        print("Error en crear la taula:", e)  # Capturar i imprimir errors
    finally:
        cur.close()  # Tancar l'objecte cursor
        conn.close()  # Tancar la connexió a la base de dades

create_table()
