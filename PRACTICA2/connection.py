import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="user_postgres",
            password="pass_postgres",
            host="db", 
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Error en connectar a la base de dades:", e)
