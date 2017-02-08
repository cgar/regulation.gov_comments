#!/usr/bin/env python3
# Parses the downloaded .json file and inserts each regulation into the
# corresponding database table/columns.

import sqlite3
from json import JSONDecoder
from functools import partial

# Start database connection
conn = sqlite3.connect('data.db')
c = conn.cursor()


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
        agencyAcronym = data.get('agencyAcronym')
        allowLateComment = data.get('allowLateComment')
        attachmentCount = data.get('attachmentCount')
        commentDueDate = data.get('commentDueDate')
        commentStartDate = data.get('commentStartDate')
        commentText = data.get('commentText')
        docketId = data.get('docketID')
        docketTitle = data.get('docketTitle')
        docketType = data.get('docketType')
        documentId = data.get('documentId')
        documentStatus = data.get('documentStatus')
        documentType = data.get('documentType')
        numberOfCommentsReceived = data.get('numberOfCommentsReceived')
        openForComment = data.get('openForComment')
        organization = data.get('organization')
        postedDate = data.get('postedDate')
        rin = data.get('rin')
        submitterName = data.get('submitterName')
        summary = data.get('summary')
        title = data.get('title')
        frNumber = data.get('frNumber')
        totalNumRecords = data.get('totalNumRecords')
        c.execute('''INSERT INTO regulations (
        agencyAcronym,
        allowLateComment,
        attachmentCount,
        commentDueDate,
        commentStartDate,
        commentText,
        docketId,
        docketTitle,
        docketType,
        documentId,
        documentStatus,
        documentType,
        numberOfCommentsReceived,
        openForComment,
        organization,
        postedDate,
        rin,
        submitterName,
        summary,
        title,
        frNumber,
        totalNumRecords) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (agencyAcronym, allowLateComment, attachmentCount, commentDueDate,
              commentStartDate, commentText, docketId, docketTitle, docketType,
              documentId, documentStatus, documentType,
              numberOfCommentsReceived, openForComment, organization,
              postedDate, rin, submitterName, summary, title, frNumber,
              totalNumRecords))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
