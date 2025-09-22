# import random


# """
# Programming Activity 1

# Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
#  - Zoomer 1997
#  - Millennial 1981
#  - Gen X 1965
#  - Baby Boomer 1946
# """
# # get input for year of birth
# birth_year = int(input("enter year you were born: "))
# # if/elif for each year and print generation
# if birth_year < 1946:
#     print("You're old")
# elif 1956 < birth_year < 1965:
#     print("You're a boomer")
# elif 1965 < birth_year < 1981:
#     print("You're a gen X'er")
# elif 1981 < birth_year < 1997:
#     print("You're a milenial")
# elif 1997 < birth_year < 2013:
#     print("You're a zoomer")
# elif 2013 < birth_year < 2025:
#     print("You're gen Alpha")
# elif birth_year > 2025:
#     print("You're gen beta")





# """
# Programming Activity 2:

# Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
#  - continue the loop while age is greater than 1
#  - print each time "you were alive in year: " current_year
#  - decrease age and current_year by one each time
#  - add an else saying "you were born in year: " current_year
# """
# age = 99
# year = 2025
# age = int(input("Input your age: "))
# while age >= 1:
#     print(f"You were alive in the year {year}")
#     age-=1
#     year-=1
# print(f"You were born in the year {year}")


# """
# Programming Activity 3

# Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
# """

# for i in range(5,96):
#     result = i%5
#     if result == 0:
#         print(i)


# """
# Programming Activity 4

# Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
# """
# x = 5
# while(x<=95):

#     result = x%5
#     if result == 0:
#         print(x)
#     x+=1

# #Additional Challenge Questions:

# """
# Write in pseudocode and then in Python a program that simulates a guessing game. The program should randomly choose a number between 1 and 100. The user must guess the number, and the program will tell the user if their guess is too high, too low, or correct. The game should continue until the user guesses the correct number or chooses to quit. The program should also keep track of how many guesses the user made.

# """
# # assign a random number
# # make a guess variable
# # loop until guess equals the random number
# # take input assign to guess
# # if guess is lower than the number say its too low
# # if guess is higher than the number say its too high
# # if guess equals the number say they got it
# secret_number = random.randint(1, 100)
# guess = 101
# while guess != secret_number:
#     guess = int(input("guess my secret number >"))
#     if guess > secret_number:
#         print("nuber too high, guess again")
#     elif guess < secret_number:
#         print("number too low, guess again")
#     elif guess == secret_number:
#         print(f"You got it! The number was {secret_number} all along!")




# """
# 1. Find all the prime numbers within a given range using a for loop

# 2. Write a Python program to reverse a given three or more digit integer WITHOUT using lists (hint, use // and % to isolate numbers)
# """
# #############################################################################################################################################
# #make a prime or not variable
# prime = False
# #take min and max for range to check
# sm = int(input("Enter minimum number in range: "))
# lg = int(input("Enter maximum number in range: "))
# #make a range of denominators to divide and find prime numbers
# denominators = [2, 3, 4, 5, 6, 7, 8, 9]
# #make a loop that goes from min number to max
# for x in range(sm,lg+1):
#     for i in denominators:
#         #make sure its not dividing by itself
#         if x != i:
#             #check if our number can evenly divide into one of the denominators
#             if x%i == 0:
#                 #if there is no remainder, set prime to false
#                 prime = False
#                 # print(f"{x} is not a prime number (divided successfully by {i})")
#                 break
#             elif x%i != 0:
#                 #if there is a remainder, the number didn't divide evenly, so we set prime to true
#                 prime = True
#                 # print(f"{x} is prime so far (divided by {i})")
#         # else:
#             # print("Skipped dividing by self")
#     if prime == True:
#         print(f"{x} is a prime number")
#     else:
#         print(f"{x} is not a prime number")
# #############################################################################################################################################

# #reverse a number
# """
# check that it's 3 or more digits
# store number of digits
# make a new string(?) list(?) from the last number moving back by taking the floor division(//) of length(the number) 
# """

import sys
# #create an empty list and empty string
# reverse = ""
list = []
# #take input and check that it's an at least 3 digit number
number = int(input("Enter a number that is at least three digits: "))

if len(str(number)) < 3:
    print("That number is less than 3 digits, try again.")
    sys.exit()
str_length = len(str(number))

###FIRST DIGIT FUNCTION
def first_digit(number):
    return number//(10**((len(str(number)))-1))
# print (f"first digit: {first_digit(number)}")

###LAST DIGIT FUNCTION
def last_digit(number):
    strang = str(number)
    return strang[len(str(number))-1]
# print(f"last digit: {last_digit(number)}")

list.append(last_digit(number))

for i in range(len(str(number))):
    number = number//10
    list.append(last_digit(number))
list.pop()
# print(list)
reverse = "" 
reverse = reverse.join(list)
print(f"reversed number: {reverse}")
