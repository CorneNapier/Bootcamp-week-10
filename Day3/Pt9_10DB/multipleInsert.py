from connect import *
from readSongs import *

def multiple_records():
    #create a list with records of songs to insert
    songsList = [   
    ('Aurora Dawn', 'Sunset Melodies', 'jazz'),
    ('Sage Serenade', 'Ethereal Emotions', 'country'),
    ('Phoenix Blaze', 'Journey to Peace', 'metal'),
    ('Kai Harmony', 'Serenade of Solitude', 'r&b'),
    ('Harmony Rain', 'Dance of Delight', 'folk'),
    ('Luna Sky', 'Serenade of the Sky', 'folk'),
    ('Caden Melody', 'Journey to Peace', 'jazz'),
    ('Ryder Echo', 'Enchanted Embrace', 'rock'),
    ('Harmony Rain', 'Echoes of Enchantment', 'pop'),
    ('Lola Lyric', 'Echoes of Ecstasy', 'electronic'),
    ('Sage Serenade', 'Whimsical Wanderings', 'jazz'),
    ('Sage Serenade', 'Mystical Musings', 'r&b')
    ]
    #insert the record from the songsList above into the songs table
    dbCursor.executemany("INSERT INTO songs(Artist, Title, Genre) VALUES(?,?,?)", songsList)
    #When you are not writing the field names use code below
    #dbCursor.executemany("INSERT INTO songs VALUES(null,?,?,?)", songsList)
    
        #display inserted records from the table
    read_songs() # call the read_song function from readSongs
multiple_records()