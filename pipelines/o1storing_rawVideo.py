# from connection.postgres import cur
from os import path
from connection.postgres import cur
from data.index import getTrending
import json
from connection.mongoDb import Db
from datetime import datetime


def createTableandInsert() -> str | bool:
    """
    Creating the table and returning the insert query
    for the transformed data

    return: str | bool
    """
    try:
        base_path = "/".join(
            path.dirname(path.realpath(__file__)).split("/")[:-1] + ["sql/"]
        )
        video = None

        with open(base_path + "createRawVideo.sql", "r") as f:
            cur.execute(f.read())

        with open(base_path + "insertRawVideo.sql", "r") as f:
            video = f.read()

        return video

    except Exception as e:
        print("Error creating table or insert query for video: \n", e)
        return False


def storeRawVideo() -> None:
    """
    Storing the Raw Video data in the Postgres DB
    with the trending id
    """
    channelIds: list = []

    try:
        trendingApi = getTrending("IN")
        if trendingApi is None:
            print("Error fetching trending data")
            return

        video_query = createTableandInsert()
        if video_query is False:
            print("Error creating table or insert query")
            return

        trending_id = rawStoreMongo(trendingApi)

        for item in trendingApi["items"]:

            # This is to avoid duplicate channel
            if item["snippet"]["channelId"] not in channelIds:
                channelIds.append(item["snippet"]["channelId"])

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
                video_query,
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

            print(
                f"⚡ Raw video with ID '{video['videoId']}' stored successfully in Postgres."
            )

        return channelIds
        # cur.execute(res[1], [data])

    except Exception as e:
        print("Something went wrong 😬: \n", e)
        return False


def rawStoreMongo(data: dict) -> bool | str:
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
