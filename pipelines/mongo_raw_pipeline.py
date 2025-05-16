from connection.mongoDb import Db
from datetime import datetime


# Storing the trending data with timestamp
def StoreTrending(data: dict):
    trendingData = {"timestamp": datetime.now(), "trending_data": data}
    try:
        print("Inserting trending data into MongoDB")
        Db["Trending"].insert_one(trendingData)
        print("Inserted trending data into MongoDB")
        # print(f"Inserted trending data with ID: {result}")
        return True
    except:
        return False


# data = getTrending(regionCode)
# StoreTrending(data)
