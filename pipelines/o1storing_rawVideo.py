# from connection.postgres import cur
from os import path
from connection.postgres import cur
from data.index import getTrending
import json
from connection.mongoDb import Db
from datetime import datetime


def CreateTableandInsert() -> dict | bool:
    """
    Creating the table and returning the insert query
    for the transformed data
    """
    try:
        base_path = "/".join(path.dirname(path.realpath(__file__)).split("/")[:-1])
        video = None

        with open(base_path + "/sql/createRawTransformed_video.sql", "r") as f:
            cur.execute(f.read())

        with open(base_path + "/sql/insertRawTransformed_video.sql", "r") as f:
            video = f.read()

        return video

    except Exception as e:
        print("Something went wrong 😬: \n", e)
        return False


def StoreRawVideo(trending_id: str, data: dict) -> None:
    """
    Storing the Raw Video data in the Postgres DB
    with the trending id
    """
    try:
        trendingApi = getTrending("IN")
        if trendingApi is None:
            print("Error fetching trending data")
            return

        video = CreateTableandInsert()
        if video is False:
            print("Error creating table or insert query")
            return

        trending_id = RawStoreMongo(trendingApi)

        for item in data["items"]:
            video = {
                "videoId": item["id"],
                "title": item["snippet"]["title"],
                "trendingId": str(trending_id),
                "publishedAt": item["snippet"]["publishedAt"],
                "channelId": item["snippet"]["channelId"],
                "channelName": item["snippet"]["channelTitle"],
                "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
                "tags": item["snippet"].get("tags", []),
                "duration": item["contentDetails"].get("duration", "PT0S"),
                "viewCount": item["statistics"].get("viewCount", 0),
                "likeCount": item["statistics"].get("likeCount", 0),
                "commentCount": item["statistics"].get("commentCount", 0),
            }
            cur.execute(
                video,
                (
                    video["videoId"],
                    video["title"],
                    video["trendingId"],
                    video["publishedAt"],
                    video["channelId"],
                    video["channelName"],
                    video["thumbnail"],
                    json.dumps(video["tags"]),
                    video["duration"],
                    video["viewCount"],
                    video["likeCount"],
                    video["commentCount"],
                ),
            )

            print("Raw Video Stored Successfully")
            # cur.execute(res[1], [data])

    except Exception as e:
        print("Something went wrong 😬: \n", e)


def RawStoreMongo(data: dict) -> bool | str:
    """
    Storing the Raw API trending data into MongoDB with timestamp

    """

    trendingData = {"trendingDataRaw": data, "createdAt": datetime.now()}
    try:
        res = Db["Trending"].insert_one(trendingData)

        print("Inserted trending data into MongoDB")
        # print(f"Inserted trending data with ID: {result}")
        return res.inserted_id
    except:
        print("Error inserting trending data into MongoDB")
        return False


# cur.execute("SELECT NOW()")
# print(cur.fetchone())
