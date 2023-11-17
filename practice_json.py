"""
1. Get your Youtube video data in JSON format
 +  RSS-to-JSOn online: rss2json.com
 +  https://www.youtube.com/feeds/videos.xml?channel_id=______
 +  API call: => link (automatically update content) to ur youtube channel
2. free fake API for testing
    https://jsonplaceholder.typicode.com/todos
"""
import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")
print('Success' if response else 'Error')
data = response.text          # JSON string
print(data)
# parse the JSON string into a list of dictionaries using json.loads(json_str) method
# JSON object -> Python dict, JSON array -> Python list
# objects = json.loads(data)     # json.loads(json_str)  json.load(json_file)
objects = response.json()     # list of dictionaries
print(response.headers['Content-Type'])      # response.headers -> dictionary-like object

# create a json file
# AttributeError: 'str' object has no attribute 'write'
# json.dump(objects[0],"api_response.json")
with open('fake_api.json', 'w') as json_file:
    json.dump(objects, json_file, indent=4)
