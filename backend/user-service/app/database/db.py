import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres-db",
        database="taxi_db",
        user="taxi_user",
        password="taxi_pass",
        port=5432
    )
    return conn
