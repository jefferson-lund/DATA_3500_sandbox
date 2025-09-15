"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""
#get input for year of birth
birth_year = int(input("enter year you were born: "))
# if/elif for each year and print generation
if birth_year < 1946:
    print("You're old")
elif 1956 < birth_year < 1965:
    print("You're a boomer")
elif 1965 < birth_year < 1981:
    print("You're a gen X'er")
elif 1981 < birth_year < 1997:
    print("You're a milenial")
elif 1997 < birth_year < 2013:
    print("You're a zoomer")
elif 2013 < birth_year < 2025:
    print("You're gen Alpha")
elif birth_year > 2025:
    print("You're gen beta")





"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""
"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
 

#Additional Challenge Questions:

"""
Write in pseudocode and then in Python a program that simulates a guessing game. The program should randomly choose a number between 1 and 100. The user must guess the number, and the program will tell the user if their guess is too high, too low, or correct. The game should continue until the user guesses the correct number or chooses to quit. The program should also keep track of how many guesses the user made.

"""
"""
1. Find all the prime numbers within a given range using a for loop

2. Write a Python program to reverse a given three or more digit integer WITHOUT using lists (hint, use // and % to isolate numbers)
"""