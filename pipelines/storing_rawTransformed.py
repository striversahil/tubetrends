# from connection.postgres import cur
from os import path
from connection.postgres import cur
import json


def CreateTableandInsert() -> dict | bool:
    try:

        base_path = "/".join(path.dirname(path.realpath(__file__)).split("/")[:-1])
        video = None
        trending = None

        with open(base_path + "/sql/createRawTransformed_trending.sql", "r") as f:
            cur.execute(f.read())

        with open(base_path + "/sql/createRawTransformed_video.sql", "r") as f:
            cur.execute(f.read())

        with open(base_path + "/sql/insertRawTransformed_trending.sql", "r") as f:
            trending = f.read()

        with open(base_path + "/sql/insertRawTransformed_video.sql", "r") as f:
            video = f.read()

        return {"trending": trending, "video": video}

    except Exception as e:
        print("Something went wrong 😬: \n", e)
        return False


def StoreRawTransformed(data: dict) -> None:
    """
    Storing the transformed data in PostgreSQL
    """
    try:
        res = CreateTableandInsert()
        if res is not False:
            cur.execute(res["trending"], ([json.dumps(data)]))
            trending_id = cur.fetchone()[0]

            for item in data["items"]:
                video = {
                    "videoId": item["id"],
                    "title": item["snippet"]["title"],
                    "trendingId": trending_id,
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
                    res["video"],
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

            print("Data Stored Successfully")
            # cur.execute(res[1], [data])

    except Exception as e:
        print("Something went wrong 😬: \n", e)


# cur.execute("SELECT NOW()")
# print(cur.fetchone())
