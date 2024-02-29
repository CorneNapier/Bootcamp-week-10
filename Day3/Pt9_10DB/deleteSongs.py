from connect import *

def delete_songs():
    try:
       #SongID is primary key field
       songID = int(input("Enter the SongID of the record to be deleted: "))
       dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {songID}")
 
       #The fetchone method a unique(one) record
       row = dbCursor.fetchone()
 
       #None is a singleton object that checks if a value is present
       if row == None:
           print(f"Delete not possible as no record with the SongID {songID} exists")
       else:
           dbCursor.execute("DELETE FROM songs WHERE SongID = ?", (songID,))
           dbCon.commit()
           print(f'The record {songID} deleted from songs table.')
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")    

if __name__ == "__main__":
    delete_songs()       
 