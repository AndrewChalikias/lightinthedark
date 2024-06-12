import requests
import json

def search(q, API):
    url = "https://www.googleapis.com/customsearch/v1?"

    params = {
        "key": API,
        "cx": "YOUR-CSE-ID",
        "lr": "lang_en",
        "q": q,
    }
    response = requests.get(url, params=params)
    # Convert the response to a JSON
    result = response.json()
    # From the JSON response, return the "items" object
    # where the results are stored.
    return result["items"]
