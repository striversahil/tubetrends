from connection.postgres import cur


try:
    cur.execute("CREATE TABLE IF NOT EXISTS test (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), num integer, data varchar);")
    cur.execute("INSERT INTO test (num, data) VALUES (42, 'Hello World!')")


    print("Table created! 🎉")
except Exception as e:
    print("Something went wrong 😬: \n", e)

# cur.execute("SELECT NOW()")
# print(cur.fetchone())
