import psycopg2
import os

conn = None
cur = None

try:
    # Connect to your postgres DB
    conn = psycopg2.connect(os.getenv("POSTGRES_URI"))

    if conn.status == 1:
        print("Postgres Connection Successful")
    else:
        print("Postgres Connection Failed")

    cur = conn.cursor()
    conn.autocommit = True
except Exception as e:
    print("Postgres Connection Error : \n", e)
    conn = None
    cur = None
