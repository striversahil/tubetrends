from connection.mongoDb import Db
from datetime import datetime


# Storing the trending data with timestamp
def StoreTrending(data: dict):
    trendingData = {"timestamp": datetime.now(), "trending_data": data}
    try:
        Db["Trending"].insert_one(trendingData)
        return True
    except:
        return False


# data = getTrending(regionCode)
# StoreTrending(data)
