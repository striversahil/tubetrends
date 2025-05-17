# from connection.postgres import cur
from os import path
from connection.postgres import cur
from data.index import getTrending
import json
import os
from connection.mongoDb import Db
from datetime import datetime
import isodate
import traceback


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


def storeRawVideo() -> list | bool:
    """
    Storing the Raw Video data in the Postgres DB
    with the trending id
    """
    channelIds: list = []

    try:
        trendingApi = getTrending("IN")
        if trendingApi is None:
            print("Error fetching trending data")
            return False

        video_query = createTableandInsert()
        if video_query is False:
            print("Error creating table or insert query")
            return False

        trending_id = rawStoreMongo(trendingApi)

        for index, item in enumerate(trendingApi["items"]):

            # This is to avoid duplicate channel
            if item["snippet"]["channelId"] not in channelIds:
                channelIds.append(item["snippet"]["channelId"])

            video = {
                "ranking": index + 1,
                "videoId": item["id"],
                "title": item["snippet"]["title"],
                "trendingId": str(trending_id),
                "publishedAt": item["snippet"]["publishedAt"],
                "category": categoryParser(item["snippet"]["categoryId"]),
                "channelId": item["snippet"]["channelId"],
                "channelName": item["snippet"]["channelTitle"],
                "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
                "tags": item["snippet"].get("tags", []),
                "duration": convert_duration(
                    item["contentDetails"].get("duration", "PT0S")
                ),
                "viewCount": int(item["statistics"].get("viewCount", 0)),
                "likeCount": int(item["statistics"].get("likeCount", 0)),
                "commentCount": int(item["statistics"].get("commentCount", 0)),
            }
            cur.execute(
                video_query,
                (
                    video["ranking"],
                    video["videoId"],
                    video["title"],
                    video["trendingId"],
                    video["publishedAt"],
                    video["category"],
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
        traceback.print_exc()
        return False


def convert_duration(duration: str) -> int:
    """
    Convert ISO 8601 duration to seconds

    :param duration: ISO 8601 duration string (e.g., "PT1H30M")
    :return: Duration in seconds
    """
    try:
        duration = isodate.parse_duration(duration)
        return int(duration.total_seconds())
    except Exception as e:
        print("Error converting duration: ", e)
        return 0


def rawStoreMongo(data: dict) -> bool | str:
    """
    Storing the Raw API trending data into MongoDB with timestamp

    """

    trendingData = {"trendingDataRaw": data, "createdAt": datetime.now()}
    try:
        res = Db[os.getenv("MONGODB_COLLECTION_NAME_VIDEO")].insert_one(trendingData)

        print("Inserted trending data into MongoDB")
        # print(f"Inserted trending data with ID: {result}")
        return res.inserted_id
    except:
        print("Error inserting trending data into MongoDB")
        return False


def categoryParser(categoryId: str) -> str:
    """
    Parse the category ID to category name
    """
    categories = {
        "1": "Film & Animation",
        "2": "Autos & Vehicles",
        "10": "Music",
        "15": "Pets & Animals",
        "17": "Sports",
        "18": "Short Movies",
        "19": "Travel & Events",
        "20": "Gaming",
        "21": "Videoblogging",
        "22": "People & Blogs",
        "23": "Comedy",
        "24": "Entertainment",
        "25": "News & Politics",
        "26": "Howto & Style",
        "27": "Education",
        "28": "Science & Technology",
        "30": "Movies",
        "31": "Anime/Animation",
        "32": "Action/Adventure",
        "33": "Classics",
        "34": "Comedy",
        "35": "Documentary",
        "36": "Drama",
        "37": "Family",
        "38": "Foreign",
        "39": "Horror",
        "40": "Sci-Fi/Fantasy",
        "41": "Thriller",
        "42": "Shorts",
        "43": "Shows",
        "44": "Trailers",
    }
    return categories.get(categoryId, "Unknown")


# cur.execute("SELECT NOW()")
# print(cur.fetchone())
