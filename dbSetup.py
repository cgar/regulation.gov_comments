#!/usr/bin/env python3
# Creates the necessary sqlite database/tables for the regulation comments.

import sqlite3
import json

conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create the necessary database tables
c.execute('''CREATE TABLE regulations (
    `agencyAcronym` VARCHAR(5),
    `allowLateComment` VARCHAR(5),
    `attachmentCount` INT,
    `commentDueDate` VARCHAR(25),
    `commentStartDate` VARCHAR(25),
    `commentText` VARCHAR(4885),
    `docketId` VARCHAR(22),
    `docketTitle` VARCHAR(391),
    `docketType` VARCHAR(13),
    `documentId` VARCHAR(27),
    `documentStatus` VARCHAR(6),
    `documentType` VARCHAR(29),
    `numberOfCommentsReceived` INT,
    `openForComment` VARCHAR(5),
    `organization` VARCHAR(112),
    `postedDate` VARCHAR(25),
    `rin` VARCHAR(12),
    `submitterName` VARCHAR(26),
    `summary` VARCHAR(284),
    `title` VARCHAR(296),
    `frNumber` VARCHAR(10),
    `totalNumRecords` INT)''')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
