
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

uri = "mongodb+srv://striversahil:AE7ty5zvAkK6vDaL@cluster0.ldfzomn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

Db = client["TubeTrends"]
# channelDb = client["Channel"]

# Storing the trending data with timestamp
def StoreTrending(data : dict):
      trendingData = {
          "timestamp" : datetime.now(),
          "trending_data" : data
      }
      try:
            Db["Trending"].insert_one(trendingData)
            return True
      except :
            return None
      
# data = getTrending(regionCode)
# StoreTrending(data)