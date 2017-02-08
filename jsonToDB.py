#!/usr/bin/env python3
# Parses and inserts each regulation the corresponding table.

import json
import sqlite3
from json import JSONDecoder
from functools import partial

# Start database connection
# conn = sqlite3.connect('data.db')
# c = conn.cursor()

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

with open('comments.json', 'r') as infh:
    for data in json_parse(infh):
        print(type(data))

# Market Hub Prices
# with open('comments.json', 'r') as infh:
#     for data in json_parse(infh):
#         buy = data['buy']['fivePercent']
#         sell = data['sell']['fivePercent']
#         vol = data['all']['volume']
#         c.execute('INSERT INTO Jita (Jita_Buy, Jita_Sell, Volume) VALUES (?, ?, ?)',
#                 (buy, sell, vol))
#
# with open('amarrPrices.json', 'r') as infh:
#     for data in json_parse(infh):
#         buy = data['buy']['fivePercent']
#         sell = data['sell']['fivePercent']
#         vol = data['all']['volume']
#         c.execute('INSERT INTO Amarr (Amarr_Buy, Amarr_Sell, Volume) VALUES (?, ?, ?)',
#                 (buy, sell, vol))
#
# # Save (commit) the changes
# conn.commit()
#
# # Close the connection
# conn.close()
