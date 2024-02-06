import psycopg2
from connection import get_connection

def delete_record():
    conn = get_connection()  # Obtenir una connexió a la base de dades
    cur = conn.cursor()  # Crear un objecte cursor per executar consultes SQL

    try:
        cur.execute("""
            DELETE FROM Videojocs
            WHERE nom = %s;
        """, ("nom_joc",))
        conn.commit()  # Confirmar els canvis a la base de dades
        print("Registre esborrat amb èxit.")  # Imprimir missatge de confirmació
    except psycopg2.Error as e:
        print("Error en esborrar el registre:", e)  # Capturar i imprimir errors
    finally:
        cur.close()  # Tancar l'objecte cursor
        conn.close()  # Tancar la connexió a la base de dades

delete_record()
