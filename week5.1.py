# print("Enter numbers to average. Enter -1 to end")
# counter = 1
# total = 0
# while True:
#     counter += 1
#     num = int(input("Enter a number: "))
#     if num == -1:
#         break
#     total += num
# avg = total/counter
# print(f"avg = {avg}")


# for i in range(1,10+1):
#     if i == 7:
#         continue
#     else:
#         print(i)

# boolean operators
"""
and
not
or
"""

age = 18
citizenship = True

# programming activities week 5


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
denom = 2
for i in range(1000):
    sum += 1 / denom
    denom *= 2
print(sum)



"""
activity 3
Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""
# age = 0
# weight = 0
# can_sit = False

# age = int(input("Enter child's age: "))
# weight = int(input("Enter child's weight: "))

# over_12 = age >= 12
# is11 = age == 11
# over_90lbs = weight > 90
# over_100lbs = weight > 100


# if over_12:
#     can_sit = True
# elif is11 and over_90lbs:
#     can_sit = True
# elif not over_12 and over_100lbs:
#     can_sit = True

# if can_sit:
#     print("Your kid can sit in the front seat!")
# else:
#     print("Your kid can't sit in the front seat.")