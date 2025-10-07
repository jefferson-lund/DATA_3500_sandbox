"""
Programming Activity 1

Write a program, and have the user enter their name and their favorite 
color, as two separate variables. Write the sentence to a file using the 
with command "<name>'s favorite color is <color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""

# name = input("Enter your name: ")
# color = input("Enter your favorite color: ")
# with open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/Activity_7.1/color_file", "w") as file:
#     file.write(f"{name}'s favorite color is {color}")



"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
array from 0s to random numbers.
"""

# import numpy
# import random

<<<<<<< HEAD
# array = numpy.zeros(100)
# print(array)
# #learned about enumerate and differences between for loops on lists vs arrays in memory
# for i, value in enumerate(array):
#     array[i] = random.randint(0,100)

# print(array)

"""
Write a program, which loads a json file "person.json" into a Python 
dictionary. Change the contents of person["age"] by adding 1. Save the 
updated dictionary to person.json, and verify the contents of person.json 
have been updated.
- load person.json in to a Python dictionary using the json.load() function
- update the value of person["age"], increase by 1
- save the Python dictionary to person.json
- open person.json and verify the "age" value has increased by 1
"""
import json

with open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/person-1.json", "r") as file:
    person = json.load(file)
    person["age"] += 1

with open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/person-1.json", "w") as file:
    json.dump(person, file)
# print(person["age"])

#verify that the age updated
with open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/person-1.json", "r") as file:
    person = json.load(file)
    print(f"Contents of json file: {person}")
=======
>>>>>>> 0b3a5fde3bc109cb9d93372e3926e596f389fd2e


