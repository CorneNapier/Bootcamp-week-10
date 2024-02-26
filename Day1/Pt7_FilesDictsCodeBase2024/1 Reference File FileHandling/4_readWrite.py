# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files


with open('Day1/Pt7_FilesDictsCodeBase2024/yourName.txt',"r+") as filePath1:# folder/folder/filename
    print(filePath1.read()) #read from fiile
    readContents = filePath1.read()
    print(readContents)
    contents ="\nIt makes sense!"
    filePath1.write(contents) #write to file 



"To Do: Task 1: Modify the code above to"
# Read the contents from your file (yourName.txt) and write to your file  
# use the with the correct mode and ensure you use both the read and the write() methods to perform their respective 
# operations
# a+ = The 'a+' mode opens the file for both reading and writing, positioning the file pointer at the end for writing in existing files and creating a new, empty file if it doesn't exist.
# w+ = In 'w+' mode, the file is opened for both reading and writing, existing content is cleared, a new empty file is created if it doesn't exist, and the file pointer is positioned at the beginning.

