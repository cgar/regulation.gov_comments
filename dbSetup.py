#!/usr/bin/env python3
# Creates the necessary sqlite database/tables for the regulation comments.

import sqlite3
import json

conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create the necessary database tables
c.execute('''CREATE TABLE regulations (
    `documents_agencyAcronym` VARCHAR(5),
    `documents_allowLateComment` VARCHAR(5),
    `documents_attachmentCount` INT,
    `documents_commentDueDate` VARCHAR(25),
    `documents_commentStartDate` VARCHAR(25),
    `documents_commentText` VARCHAR(4885),
    `documents_docketId` VARCHAR(22),
    `documents_docketTitle` VARCHAR(391),
    `documents_docketType` VARCHAR(13),
    `documents_documentId` VARCHAR(27),
    `documents_documentStatus` VARCHAR(6),
    `documents_documentType` VARCHAR(29),
    `documents_numberOfCommentsReceived` INT,
    `documents_openForComment` VARCHAR(5),
    `documents_organization` VARCHAR(112),
    `documents_postedDate` VARCHAR(25),
    `documents_rin` VARCHAR(12),
    `documents_submitterName` VARCHAR(26),
    `documents_summary` VARCHAR(284),
    `documents_title` VARCHAR(296),
    `documents_frNumber` VARCHAR(10),
    `totalNumRecords` INT)''')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
