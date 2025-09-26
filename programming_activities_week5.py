"""
Programming Activity 1

Write a program which can tell if a 3 digit number is a palindrome. 
 - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
 - Convert the user input into a integer (int). To get the first digit alone, floor division by 100. 
 - To get the 3rd digit alone, modulus by 10. 
 - Check if the first digit and 3rd digit are the same. 
 - If they are the same print("palindrome!!!!"). 
 - Else print("not palindrome!")
"""
import sys
number = int(input("Enter a 3 digit number: "))
if len(str(number)) != 3:
    print("That is not 3 digits")
    sys.exit()
dig1 = number//100
dig3 = number%10
if dig1 == dig3:
    print("This is a palindrome.")
else:
    print("Not a palindrome.")

"""
Programming Activity 2

Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
 """
sum = 0
denominator = 0
for i in range(1,1000-1):
    denominator = i
    sum += (1/denominator)
print(sum)

"""
Programming Activity 3

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""

age = 0
weight = 0
can_sit = False

age = int(input("Enter child's age: "))
weight = int(input("Enter child's weight: "))

over_12 = age >= 12
is11 = age == 11
over_90lbs = weight > 90
over_100lbs = weight > 100


if over_12:
    can_sit = True
elif is11 and over_90lbs:
    can_sit = True
elif not over_12 and over_100lbs:
    can_sit = True

if can_sit:
    print("Your kid can sit in the front seat!")
else:
    print("Your kid can't sit in the front seat.")

"""
Programming Activity 4

Write a function named "welcome_fctn" which takes one argument, called "name".  Inside the function, print to the console "Welcome " name.
- Use the def command to define a function "welcome_fctn"
- Add a parameter list with one variable "name", i.e. (name)
- Print "Welcome " name in the function body.
- We don't need a return statement here, but keep in mind python does return nothing.
- Call the function, welcome_fctn(<your_name>)
"""

def welcome_fctn(name):
    print(f"Welcome, {name}")

welcome_fctn("Jefferson")


"""
Programming Activity 5

Update the function in activity one, and create a new string variable in the function called, welcome_message. The variable welcome_message should be 
assigned the value "Welcome " name. The same value printed in activity 1, but here you save it as a variable. Return the variable welcome_message.
- Assuming your function in programming activity 1 works, you will need to:
- Create a variable to store "Welcome " + name
- Return the value welcome_message
- There are a couple ways to test this. you could
         1. Print(welcome_fctn("Bob"))
         2. Create a variable to store what is returned by the function then print that
"""

def welcome_fctn(name):
    message = f"Welcome, {name}"
    return message

print(welcome_fctn("Jefferson"))



"""
Programming Activity 6

Update the function in activity one to have 3 variables: name (string),  age (int), favorite_color (string).  Create a new variable called welcome_message and assign it to the value "Welcome <name>, you are <age> years old, and <favorite_color> is your favorite color".  Return the variable welcome_message.
- Add two variables to your parameter list
- Concatenate those two variables in your welcome_message
- Return welcome_message just like you did in activity 2
- To test this, call welcome_fctn with 3 arguments
"""

def welcome_fctn(name, age, favorite_color):
    return f"Welcome {name}, you are {age} years old, and {favorite_color} is your favorite color"

print(welcome_fctn("Jefferson", 25, "silver"))