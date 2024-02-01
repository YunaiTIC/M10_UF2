import psycopg2
from connection import get_connection

def read_records():
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM Videojocs;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error en llegir els registres:", e)
    finally:
        cur.close()
        conn.close()

read_records()
