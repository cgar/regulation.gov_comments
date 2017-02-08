from settings import SECRET_KEY


import os
import json
import requests


def getComments(SECRET_KEY):
    # Call the URL and get the number of comments based on the following
    # criteria: results per page = 100, sort order = DESCending,
    # sort by = Posted Date and keyword = florida
    urlPartOne = "https://api.data.gov/regulations/v3/documents.json?api_key="
    urlPartTwo = "&rpp=100&so=DESC&sb=postedDate&s=florida"
    url = urlPartOne + SECRET_KEY + urlPartTwo
    response = requests.get(url)
    response.raise_for_status()
    commentData = json.loads(response.text)
    with open('comments.json', 'w') as fp:
        json.dump(commentData, fp)
    fp.close()


getComments(SECRET_KEY)
