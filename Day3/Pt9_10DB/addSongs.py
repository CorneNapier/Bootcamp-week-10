from connect import *

#Create a subroutine to add songs to the songs table
def insert_songs():
    try:
        #SongID is an auto increment field no data is required.
        #SongID, Artist, Title, Genre
    
        #Create variables for each field to store the respective data from the input function
        sTitle = input("Enter song title: ")
        sArtist = input("Enter song artist: ")
        sGenre = input("Enter song genre: ")
    
        dbCursor.execute("INSERT INTO songs VALUES(NULL, ?,?,?)", (sTitle, sArtist, sGenre))
    
        dbCon.commit() # make the changes in the db permanent
    
        print(f'{sTitle} inserted in the songs table')
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
            
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    
    except sql.Error as er:
        print(f"Failed because of Error: {er}")
        
insert_songs() # call the function