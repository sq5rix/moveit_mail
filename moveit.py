"""
Moveit class
https://www.ipswitch.com/moveit/rest-api
"""

import requests

class MoveIT:

    def __init__(self):
        self.url = "https://your-transfer-server/api/v1/"

    def test(self):
        print('self.url : ', self.url )

def main():
    m = MoveIT()
    m.test()

if __name__ == "__main__":
    main()
