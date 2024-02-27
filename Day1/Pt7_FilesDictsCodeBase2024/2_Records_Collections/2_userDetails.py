# fname    = input("Enter you full name: ")
# address   = input("Enter your address: ")
# interest = input("Enter your interest: ")
# age      =    int(input("Enter your age: "))


# create a dictionary 
dict1 = {"Fullname": "Jane Smith", "Age": 23, "Hobby":"Coding", 1:"Gamer"}

# create a dictionary with keys but no values 
print("dictionary with keys but no values")
userDetails1 = {"fname": "", "address": "", "interest":"", "age":""}
print(userDetails1)

# Use key to add values to dictionary 

userDetails1["fname"] = input("Enter you full name: ")
print(userDetails1)

"Extension"
"Modify"
"To Do: Task 1: write the input statement to add the remaining values to the userDetails1 dictionary above"
for keyVal in userDetails1: #iterate or loop through all keys and values
    userDetails1[keyVal] = input(f'Enter the value for {keyVal}: ') 
print(userDetails1)

# create a dictionary with no keys and no values
greetings = {}
print(f"{greetings}dictionary with no keys and no values")

"Make"
"To Do: Task 2: Create a dictionary with no keys as shown below, then write the input statement to add the keys and values."
userDetails2 = {}
print(userDetails2)

members = {}
numOfKeyVal = int(input("Enter the number of key value pairs: "))
keyValCount = 0 #counter for amount of key value pairs

while True:
    aKey = input('Enter key: ')
    aValue = input(f'Enter the value for {aKey}: ')
    members[aKey] = aValue
    keyValCount += 1 #increment counter
    
    if keyValCount == numOfKeyVal:
        break


print(members)

