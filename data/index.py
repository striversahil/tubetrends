from requests import get

def GetRawData():
      response = get('https://api.github.com')
      print(response.status_code)
      print(response.json())