import psycopg2
import os


def PostgresConnection():
    """
    Postgres Connection
    """
    try:
        conn = psycopg2.connect(os.getenv("POSTGRES_URI"))

        if conn.status == 1:
            print("✅ Postgres Connection Successful")
        else:
            print("⚠️ Postgres Connection Failed")

        conn.autocommit = True
        cur = conn.cursor()
        return cur
    except Exception as e:
        print("Postgres Connection Error : \n", e)

        return None


#  Global Instance of the Postgres Connection
cur = PostgresConnection()
