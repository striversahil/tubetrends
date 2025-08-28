# from connection.postgres import cur
from os import path
from connection.postgres import cur
from data.index import getChannel
import traceback
import os
from connection.mongoDb import Db
from datetime import datetime


def createTableandInsert() -> str | bool:
    """
    Creating the table and returning the insert query
    for the raw data

    return: str | bool
    """
    try:
        base_path = "/".join(
            path.dirname(path.realpath(__file__)).split("/")[:-1] + ["sql/"]
        )
        channel = None

        with open(base_path + "createRawChannel.sql", "r") as f:
            cur.execute(f.read())

        with open(base_path + "insertRawChannel.sql", "r") as f:
            channel = f.read()

        return channel

    except Exception as e:
        print("Error creating table or insert query for video: \n", e)
        return False


def storeRawChannel(channelIds: list) -> list:
    """
    Storing the Raw Video data in the Postgres DB
    with the channel id

    channelIds: list of channel ids to be stored
    return: list
    """
    try:
        channel_query = createTableandInsert()

        if channel_query is False:
            print("Error creating table or insert query")
            return

        for channelId in channelIds:
            storedChannel = lookupChannel(channelId)
            if storedChannel is not None:
                print(
                    f"💡 Channel with ID '{channelId}' already exists in Postgres. Skipping..."
                )
                continue

            channelApi = getChannel(channelId)
            if channelApi is None:
                print("Error fetching channel data")
                return

            mongo_id = rawStoreMongo(channelApi)
            if mongo_id is False:
                print("Error storing channel data in MongoDB")
                return
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            item = channelApi["items"][0]

            channel = {
                "channelId": item["id"],
                "title": item["snippet"]["title"],
                "description": item["snippet"].get("description", None),
                "createdAt": item["snippet"]["publishedAt"],
                "profilePic": item["snippet"]["thumbnails"]["default"]["url"],
                "country": item["snippet"].get("country", None),
                "viewCount": int(item["statistics"]["viewCount"]),
                "subscriberCount": int(item["statistics"]["subscriberCount"]),
                "videoCount": int(item["statistics"]["videoCount"]),
                "isKids": item.get("status", {}).get("madeForKids", False),
            }
            cur.execute(
                channel_query,
                (
                    channel["channelId"],
                    channel["title"],
                    channel["description"],
                    channel["createdAt"],
                    channel["profilePic"],
                    channel["country"],
                    channel["viewCount"],
                    channel["subscriberCount"],
                    channel["videoCount"],
                    channel["isKids"],
                ),
            )

            print(
                f"⚡ Raw channel with ID '{channel['channelId']}' stored successfully in Postgres."
            )

        # cur.execute(res[1], [data])
        return True

    except Exception as e:
        print("Something went wrong 😬: \n", e)
        traceback.print_exc()
        return False


def lookupChannel(channelId: str) -> dict | None:
    """
    Lookup the channel data from the Postgres DB
    with the channel id
    """

    try:
        cur.execute(
            "SELECT channelId, title, createdAt FROM channel WHERE channelId = %s",
            (channelId,),
        )
        channelData = cur.fetchone()

        if channelData is None:
            return None

        return {
            "channelId": channelData[0],
            "title": channelData[1],
            "createdAt": channelData[2],
        }

    except Exception as e:
        print("Error fetching channel data: \n", e)
        return None


def rawStoreMongo(data: dict) -> bool | str:
    """
    Storing the Raw API Channel data into MongoDB with timestamp

    """

    channelData = {"channelDataRaw": data, "createdAt": datetime.now()}
    try:
        # res = Db[os.getenv("MONGODB_COLLECTION_NAME_CHANNEL")].insert_one(channelData)
        # if res is None:
        #     print("Error inserting channel data into MongoDB")
        #     return False
        return "channel_id_placeholder"
    except:
        print("Error inserting Channel data into MongoDB")
        return False
