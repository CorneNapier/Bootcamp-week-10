from connect import *

def search_songs():
    try:
        # Search by SongID or Title or Artist or Genre
        field = input('Search by SongID or Title or Artist or Genre (Case Sensitive): ')
        
        if field == "SongID":
            #search by SongID
            songID = int(input('Enter SongID: '))
            dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (songID,))
            row = dbCursor.fetchone()
            
            if row == None:
                print(f'No record with the SongID {songID} provided exists in the table.')
            else:
                print(row)
        elif field in ['Title', 'Artist', 'Genre']:
            # Search by Title or Artist or Genre
            strInput = (input(f'Enter the value for the field {field}: '))
            
            dbCursor.execute(f"SELECT * FROM songs WHERE {field} LIKE '%{strInput}%' ")
            
            rows = dbCursor.fetchall()
            
            if not rows:
                print(f'No record(s) with field {field} matching {strInput}')
            else:
                for records in rows:
                    print(records)
        else:
            #where the field to search is not SongID or Title or Artist or Genre
            print(f'Search field {field} invalid!!')
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
        
search_songs()     
      