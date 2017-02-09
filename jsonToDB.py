#!/usr/bin/env python3
# Parses the downloaded .json file and inserts each regulation into the
# corresponding database table/columns.

import sqlite3
from main import json_parse

# Start database connection
conn = sqlite3.connect('data.db')
c = conn.cursor()

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
        frNumber) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (agencyAcronym, allowLateComment, attachmentCount, commentDueDate,
              commentStartDate, commentText, docketId, docketTitle, docketType,
              documentId, documentStatus, documentType,
              numberOfCommentsReceived, openForComment, organization,
              postedDate, rin, submitterName, summary, title, frNumber))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
