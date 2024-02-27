fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

#Create a dictionary
userData = {'Fullname': fname, 'Address': address, 'Interests': interest, 'Age': age}


with open("Day1/Pt7_FilesDictsCodeBase2024/1 Reference File FileHandling/userDetails1.txt", "a") as addData:
   for k, v in userData.items():
       addData.write(f'\n{k}: {v}')



"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp