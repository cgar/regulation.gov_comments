#!/usr/bin/env python3
# Parses the downloaded .json file and inserts each regulation into the
# corresponding kbase table/columns.

import sqlite3
import json

# Start database connection
conn = sqlite3.connect('data.db')
c = conn.cursor()

with open('comments.json', 'r') as infh:
    data = json.load(infh)
    for k in data.get('documents'):
        agencyAcronym = k.get('agencyAcronym')
        allowLateComment = k.get('allowLateComment')
        attachmentCount = k.get('attachmentCount')
        commentDueDate = k.get('commentDueDate')
        commentStartDate = k.get('commentStartDate')
        commentText = k.get('commentText')
        docketId = k.get('docketID')
        docketTitle = k.get('docketTitle')
        docketType = k.get('docketType')
        documentId = k.get('documentId')
        documentStatus = k.get('documentStatus')
        documentType = k.get('documentType')
        numberOfCommentsReceived = k.get('numberOfCommentsReceived')
        openForComment = k.get('openForComment')
        organization = k.get('organization')
        postedDate = k.get('postedDate')
        rin = k.get('rin')
        submitterName = k.get('submitterName')
        summary = k.get('summary')
        title = k.get('title')
        frNumber = k.get('frNumber')
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
