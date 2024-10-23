import requests
from requests.auth import HTTPBasicAuth
import json

# Local API endpoint
# url = "http://127.0.0.1:8080/text_cosine"

# Remote API endpoint (don't forget to make it public or to specify authentication auth=(id, pw) in the post method)
url = "https://supreme-space-tribble-q679vqw4qgj29vp9-8080.app.github.dev/text_cosine"

# Send a GET request to the API
query = json.dumps({
  "text": [
    "I love Mozart", "I love jazz", "I love rap"
  ]
})
response = requests.post(url, query)

# Check if the request was successful
if response.status_code == 200:
    data = response.content
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
