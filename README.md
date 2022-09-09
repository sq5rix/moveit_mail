# moveit_mail
python based ipswitch moveit

https://www.ipswitch.com/moveit/rest-api

curl -k --request POST --url https://your-transfer-server/api/v1/token --data "grant_type=password&username=emmacurtis&password=1a2B3cA1b2C3"

curl -H "Authorization: Bearer X03w.....dziTwmA"  "https://your-transfer-server/api/v1/users/self"

curl -H "Authorization: Bearer your-access-token"  "https://your-transfer-server/api/v1/folders/311392888/files"

curl -k --request POST --url https://mydmzserver/api/v1/token --data "grant_type=password&username=${username}&password=${password}"

curl -X POST https://mydmzserver/api/v1/token -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token=${refresh-token}"

