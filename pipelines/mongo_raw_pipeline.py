from connection.mongoDb import Db
from datetime import datetime


# Storing the trending data with timestamp
def StoreTrending(data: dict) -> bool | str:
    trendingData = {"trendingDataRaw": data, "createdAt": datetime.now()}
    try:
        res = Db["Trending"].insert_one(trendingData)

        print("Inserted trending data into MongoDB")
        # print(f"Inserted trending data with ID: {result}")
        return res.inserted_id
    except:
        print("Error inserting trending data into MongoDB")
        return False


# data = getTrending(regionCode)
# StoreTrending(data)
