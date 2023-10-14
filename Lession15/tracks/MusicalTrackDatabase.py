import sqlite3
import xml.etree.ElementTree as ET


conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

def create_table():

    cur.executescript("""
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, 
        rating INTEGER, 
        count INTEGER
    );
    """)


def openfile(name):
    if len(name) < 1:
        name = "tracks/Library.xml"
    return ET.parse(name)


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


def insertdata(itemin):
    name = lookup(itemin, 'Name')
    artist = lookup(itemin, 'Artist')
    album = lookup(itemin, 'Album')
    count = lookup(itemin, 'Play Count')
    rating = lookup(itemin, 'Rating')
    length = lookup(itemin, 'Total Time')
    genre = lookup(itemin, 'Genre')

    if artist is not None:
        cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist,))
        cur.execute("SELECT id FROM Artist WHERE name = ? ", (artist,))
        artist_id = cur.fetchone()[0]
    else:
        artist_id = 0

    if genre is not None:
        cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
        cur.execute("SELECT id FROM Genre WHERE name = ? ", (genre,))
        genre_id = cur.fetchone()[0]
    else:
        genre_id = 0

    if album is not None:
        cur.execute("INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)", (artist_id, album))
        cur.execute("SELECT id FROM Album WHERE title = ? ", (album,))
        album_id = cur.fetchone()[0]
    else:
        album_id = 0

    cur.execute("INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)",
                (name, album_id, genre_id, length, rating, count))

    # conn.commit()


if __name__ == '__main__':
    create_table()
    lst = openfile(input("Enter file name:")).findall("dict/dict/dict")
    for item in lst:
        if lookup(item, 'Track ID') is None:
            continue

        insertdata(item)

    conn.commit()
