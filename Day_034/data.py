import requests

OPEN_TRIVIA_API = "https://opentdb.com/api.php"

PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=OPEN_TRIVIA_API, params=PARAMETERS)
response.raise_for_status()

data = response.json()

question_data = data["results"]