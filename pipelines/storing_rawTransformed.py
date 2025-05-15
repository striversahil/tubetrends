# from connection.postgres import cur
from os import path
from connection.postgres import cur

def CreateTable():
    try:
        pat = path.dirname(path.realpath(__file__))
        pth = pat.split("/")[:-1]
        ph = "/".join(pth)

        with open(ph + "/sql/createRawTransformed_trending.sql", "r") as f:
            cur.execute(f.read())

        with open(ph + "/sql/createRawTransformed_video.sql", "r") as f:
            cur.execute(f.read())
        
        return True
        
    except Exception as e:
        print("Something went wrong 😬: \n", e)
        return False
    



def StoreRawTransformed(data : dict):
    try:
        res = CreateTable()
        if res is not None :
            for video in data["items"]:
                videoData = {
                    "video_id" : video["id"],
                    "title" : video["snippet"]["title"],
                    "description" : video["snippet"]["description"],
                    "published_at" : video["snippet"]["publishedAt"],
                    "channel_id" : video["snippet"]["channelId"],
                    "channel_title" : video["snippet"]["channelTitle"],
                    "view_count" : video["statistics"]["viewCount"],
                    "like_count" : video["statistics"]["likeCount"],
                    "comment_count" : video["statistics"]["commentCount"],
                    "favorite_count" : video["statistics"]["favoriteCount"],
                    "dislike_count" : video["statistics"]["dislikeCount"],
        
    except Exception as e:
        print("Something went wrong 😬: \n", e)

# cur.execute("SELECT NOW()")
# print(cur.fetchone())
