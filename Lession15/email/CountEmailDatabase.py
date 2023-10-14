import sqlite3
import re

# oldConn = sqlite3.connect('emaildb.sqlite')
# oldCur = oldConn.cursor()
# conn = sqlite3.connect('countResult.sqlite')
# cur = conn.cursor()

# use emaildb.py to create the table already

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

for row in cur.execute("SELECT email, count FROM EmailCounts").fetchall():
    org = re.findall("@.*", str(row[0]))[0].strip("@")
    print(org)

    cur.execute("SELECT count FROM Counts WHERE org = ?", (str(org), ))
    result = cur.fetchone()
    if result is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, ?)", (str(org), row[1]))
    else:
        cur.execute("UPDATE Counts SET count = count + ? WHERE org = ?", (row[1], str(org)))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'
total = 0

for row in cur.execute(sqlstr):
    total += row[1]

print("Total Count:", total)
