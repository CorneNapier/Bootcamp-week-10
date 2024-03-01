from connect import *
from readSongs import *

def dump_data():
    #open folder/file.....
    with open("Day3/Pt9_10DB/songs.sql") as dumpFile:
        #read the contents saved in the dumpFile variable and pass it to sqlInsert variable
        sqlInsertScripts = dumpFile.read()
        
        #write the content found/stored in sqlInsertScripts variable to the table
        dbCursor.executescript(sqlInsertScripts)
        
        #display inserted records from the table
        read_songs() # call the read_song function from readSongs
dump_data()