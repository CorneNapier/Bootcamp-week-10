from connect import *

def read_songs():
    try:
       "Method 1"
       # allSongs = dbCursor.execute("SELECT * FROM songs").fetchall()
    
       "Method 2"
       dbCursor.execute("SELECT * FROM songs") # selects all data from table songs
       allSongs = dbCursor.fetchall() # fetchall retrieves all selected rows/records
    
       if allSongs:
          #format output
          "index   0        1       2        3"
          print(" SongID | Title                          | Artist                         | Genre")
          print("*" * 100)
        
          for aSong in allSongs:
               print(f'{aSong[0]:7} | {aSong[1]:30} | {aSong[2]:30} | {aSong[3]:20}')
               print("-" * 100)
        
            
       else:
           print("No songs found in the table")
           
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
            
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    
    except sql.Error as er:
        print(f"Failed because of Error: {er}")

if __name__ == "__main__":
    read_songs()