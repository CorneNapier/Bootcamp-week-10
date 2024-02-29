from connect import *
 
def update_song():
    try:
       #SongID is primary key field
       songID = int(input("Enter the SongID of the record to be updated: "))
       dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {songID}")
 
       #The fetchone method a unique(one) record
       row = dbCursor.fetchone()
 
       #None is a singleton object that checks if a value is present
       if row == None:
           print(f"No record with the SongID {songID} exists")
       else:
           fieldName = input("Enter the field (Artist or Title or Genre): ").title()
           fieldValue = input(f"Enter the value for {fieldName}: ")
 
            #UPDATE songs SET Artist or Title or Genre = ArtistValue or TitleValue or GenreValue WHERE SongID = 1/2/3/4/5...
           dbCursor.execute(f"UPDATE songs SET {fieldName} = ? WHERE SongID = ? ", (fieldValue,songID))
           dbCon.commit()
           print(f"Record with SongID {songID} Updated")
 
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
         
update_song()