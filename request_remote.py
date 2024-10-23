import requests
import json

# Local API endpoint
# url = "http://127.0.0.1:8080/text_cosine"

# Remote API endpoint (don't forget to make it public or to specify authentication auth=(id, pw) in the post method)
url = "https://supreme-space-tribble-q679vqw4qgj29vp9-8080.app.github.dev/text_cosine"
# url = "https://8080-cs-e73794f1-3bde-4568-9e29-1591d8c898bb.cs-europe-west1-haha.cloudshell.dev/"

# Send a request to the API
query = json.dumps({
  "text": [
    "I love Mozart", "I love jazz", "I love rap"
  ]
})
response = requests.post(url, query)

# response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.content
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
