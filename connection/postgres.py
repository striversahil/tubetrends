import psycopg2
import os


conn = psycopg2.connect(os.getenv('POSTGRES_URI'))
conn.autocommit = True
cur = conn.cursor()

def getCon ():
      return conn

def getCur ():
      return cur