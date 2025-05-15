# from connection.postgres import cur
from os import path
from connection.postgres import cur

def CreateTableandInsert() -> dict | bool:
    try:
        pat = path.dirname(path.realpath(__file__))
        pth = pat.split("/")[:-1]
        ph = "/".join(pth)

        video = None
        trending = None

        with open(ph + "/sql/createRawTransformed_trending.sql", "r") as f:
            cur.execute(f.read())

        with open(ph + "/sql/createRawTransformed_video.sql", "r") as f:
            cur.execute(f.read())

        with open(ph + "/sql/insertRawTransformed_trending.sql", "r") as f:
            trending = f.read()

        with open(ph + "/sql/insertRawTransformed_video.sql", "r") as f:
            video = f.read()
        
        return { trending, video }
        
    except Exception as e:
        print("Something went wrong 😬: \n", e)
        return False
    



def StoreRawTransformed(data : dict):
    try:
        res = CreateTableandInsert()
        if res is not False: 
            cur.execute(res[0], [data])
            cur.execute(res[1], [data])
        
    except Exception as e:
        print("Something went wrong 😬: \n", e)

# cur.execute("SELECT NOW()")
# print(cur.fetchone())
