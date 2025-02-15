# Day 37 was a short day, on this day, the goal was to play around with the Pixela API and explore it's capabilities,
# having a deeper understanding of HTTP requests.

# Pixela allows you to create commit graphs, similar to the ones in GitHub/GitLab.

# This script has 3 HTTP requests, for creating, updating and deleting commits from a graph.

import datetime
from dotenv import load_dotenv
import os
import requests

load_dotenv()

PIXELA_API_KEY = os.getenv("PIXELA_API_KEY")
PIXELA_GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")
PIXELA_USER = os.getenv("PIXELA_USER")

PIXELA_HOST = f"pixe.la/v1/users/{PIXELA_USER}/graphs/{PIXELA_GRAPH_ID}"

TODAY = datetime.datetime.now().strftime("%Y%m%d")

REQUEST_HEADERS = {
    "X-USER-TOKEN" : PIXELA_API_KEY
}

POST_REQUEST_BODY = {
    "date": TODAY,
    "quantity": "1"
}

PUT_REQUEST_BODY = {
    "quantity": "2"
}

# response = requests.post(url=f"https://{PIXELA_HOST}/", json=POST_REQUEST_BODY, headers=REQUEST_HEADERS)

response = requests.put(url=f"https://{PIXELA_HOST}/{TODAY}", json=PUT_REQUEST_BODY, headers=REQUEST_HEADERS)

# response = requests.delete(url=f"https://{PIXELA_HOST}/{TODAY}", headers=REQUEST_HEADERS)

print(response)