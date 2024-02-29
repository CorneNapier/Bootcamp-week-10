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

def songs_menu():
    option = 0 #assign the option variable with an integer value 0
    #see menuOptions.txt for reference. Create a list of string values/elements/items
    optionsList = ['1', '2', '3', '4', '5', '6']
    #call the read file function and assign it to a variable called menuChoices
    menuChoices = read_file("Day3/Pt9_10DB/menuOptions.txt")
    
    #repeat the menu options until the option to exit the menu is entered
    
    while option not in optionsList:
        #print the menuOptions.txt file by calling the variable that holds the read_file function in the print statment
        print(menuChoices)
        
        #re-assign the value of the option variable so it can be re-used
        option = input("Enter an option from the menu choices above: ")
        
        #check if the input entered in the option variable above is not oustide 1,2,3,4,5,6
        if option not in optionsList:
            print(f'{option} is not a valid choice!!!')
    return option

mainProgram = True #Toggle to False to exit the while loop below
while mainProgram:
    #call the songs menu function and assign it to a variable
    mainMenu = songs_menu()
    
    #match case is the same as switch in JavaScript
    match mainMenu:
        case "1": #call the readsong file imported on line 1 and the function inside read_songs()
            readSongs.read_songs()
        case "2":
            addSongs.insert_songs()
        case "3":
            updateSongsV2.update_song()
        case "4":
            deleteSongs.delete_songs()
        case "5":
            reports.search_songs()
        case _:
            mainProgram = False #set mainProgram variable to false to exit the menu
input("Press enter to exit.....")