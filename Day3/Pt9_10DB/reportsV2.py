from connect import *

def search_songs():
    try:
        #dbCursor.execute("SELECT * FROM songs ORDER BY Title DESC")
        #dbCursor.execute("SELECT * FROM songs ORDER BY SongID DESC")
        #dbCursor.execute("SELECT * FROM songs ORDER BY Title ASC")
        #dbCursor.execute("SELECT * FROM songs WHERE Genre = 'Modern Rock' ")
        dbCursor.execute("SELECT * FROM songs WHERE Genre NOT LIKE 'Modern Rock' ")
        
        allSongs = dbCursor.fetchall()
        for songs in allSongs:
            print(songs)
     
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
        
search_songs()     
