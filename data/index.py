import requests
import os
regionCode = "IN"
channelId = "UC_x5XG1OV2P6uZZ5FSM9Ttw"


def getChannel(channelId: str)  -> dict | None:
      if channelId is None:
            return None
      
      getChannelUrl = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channelId}&key={os.getenv('YOUTUBE_API_KEY')}"

      try:
            response = requests.get(getChannelUrl)
            data = response.json()
            return data
      except :
            return None


def getTrending(regionCode: str) -> dict | None:
      if regionCode is None:
            regionCode = "US"
            
      getTrendingUrl = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&chart=mostPopular&regionCode={regionCode}&maxResults=20&key={os.getenv('YOUTUBE_API_KEY')}"

      try:
            response = requests.get(getTrendingUrl)
            data = response.json()
            return data
      except :
            return None