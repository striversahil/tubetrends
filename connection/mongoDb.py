import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Create a new client and connect to the server
def MongoDbConnection():
    """
    MongoDB Connection
    """
    try:
        client = MongoClient(os.getenv("MONGODB_URI"), server_api=ServerApi("1"))
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        Db = client[os.getenv("MONGODB_NAME")]
        return Db

    except Exception as e:
        print("MongoDB Connection Error : \n", e)
        return None


Db = MongoDbConnection()
# Global Instance of the MongoDB Connection
