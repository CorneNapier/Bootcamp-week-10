import readSongs, addSongs, updateSongsV2, deleteSongs, reports

def read_file(file_path): #file_path is a parameter/variable
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f'File not found because: {nf}')
        
#test to retrieve or load menuOptions.txt file
#print(read_file("Day3/Pt9_10DB/menuOptions.txt"))  

