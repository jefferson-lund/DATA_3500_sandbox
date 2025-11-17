

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# lst = []
# lst2 = []
# lst.append(lst2)
# for i in range(num1):
#     lst.append(i)
# for i in range(num2):
#     lst2.append(i)
# print(lst)
# print(f"lst: {lst}")
# print(f"lst2: {lst2}")

import json

# Activity 1
# get user input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

twoDList = []

for i in range(num1):
    twoDList.append([])

# nested for loop to loop through 2D list
for i in range(1, num1+1):
    for j in range(1, num2+1):
        twoDList[i-1].append(i * j)
        
# nested for loop to print out 2D list   
for i in range(num1):
    for j in range(num2):
        print(twoDList[i][j], end="   ")
    print()
  
# Activity 2
# create dictionary
dictionary = {}

# create dictionary keys and assign them to values
dictionary["age"] = int(input("What is your age: "))
dictionary["favorite_color"] = input("What is your favorite color: ")
dictionary["multiplication_table"] = twoDList

# print out all keys in dictionary and the values
for key in dictionary.keys():
    print(key, dictionary[key])
  
# Activity 3
# use with open to update person.json
with open("person.json") as file:
    person = json.load(file)

# update information about person
print(person["age"])
person["age"] += 1
print(person["age"])

with open("person.json", "w") as file:
	json.dump(person, file, indent=4)
  
# Activity 4
# get user input 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
try:
    num1/num2
except: # exception handling
    print("Cannot divide by zero")