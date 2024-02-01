import psycopg2
from connection import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Videojocs (
                nom varchar,
                descripcio varchar,
                categoria varchar ,
                autor varchar,
                preu float,
                data_sortida date
            );
        """)
        conn.commit()
        print("Taula creada amb èxit.")
    except psycopg2.Error as e:
        print("Error en crear la taula:", e)
    finally:
        cur.close()
        conn.close()

create_table()
