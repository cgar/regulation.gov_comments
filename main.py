# Main program:
# Downloads latest regulation comments with the keyword 'Florida'.
from settings import SECRET_KEY
from functools import partial
from json import JSONDecoder


import re
import json
import requests


# Fix JSON Decode Error: Extra data
def json_parse(fileobj, decoder=JSONDecoder(), buffersize=2048):
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
        buffer += chunk
        while buffer:
            try:
                result, index = decoder.raw_decode(buffer)
                yield result
                buffer = buffer[index:]
            except ValueError:
                # Not enough data to decode, read more
                break


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
