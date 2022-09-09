"""
Moveit class
https://www.ipswitch.com/moveit/rest-api
http://open-notify.org/Open-Notify-API/
"""


import json
import requests

URL_MOVE_IT =  "https://your-transfer-server/api/v1/"
URL_NASA = "http://api.open-notify.org/"
ISS_ENDPOINT = "iss-now.json/"
ASTROS_ENDPOINT = "astros.json/"

class MoveIT:

    def __init__(self):
        self.url = URL_MOVE_IT

    def get_nasa(self, endpoint, query=None):
        if query:
            response = requests.get(URL_NASA+endpoint, params=query)
        else:
            response = requests.get(URL_NASA+endpoint)

        response.raise_for_status()
        print(response.json())

def main():
    m = MoveIT()
    query = {'lat':'45', 'lon':'180'}
    t = m.get_nasa(ISS_ENDPOINT, query)
    t = m.get_nasa(ASTROS_ENDPOINT)

if __name__ == "__main__":
    main()

