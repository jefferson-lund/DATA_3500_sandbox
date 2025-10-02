"""
Programming Activity 1

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""

# colors = ["red", "green", "blue"]
# for color in colors:
#     print(color)


"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""

# colors = ["red", "green", "blue"]
# for color in colors:
#     print(color)
#     for letter in color:
#         print(letter)
    

"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""

import random

# list = []
# for i in range(10):
#     list.append(random.randint(1,100))

# print(list)

"""
Programming Activity 4 

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""

# list = []
# for i in range(10):
#     list.append(random.randint(1,100))
# for i in range(10-1):
#     if list[i]%2 == 0 and list[i+1]%2 == 0:
#         print(f"{list[i]} and {list[i+1]} are even numbers.")

# print(list)



# USE THIS FILE: AAPL.2023.txt
"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""
"""    better way to do it
count = 0
first_5 = []

file = open("/workspaces/DATA_3500_sandbox/AAPL.2023.txt", "r")
# print(f"file: {file}")
lines = file.readlines()

prices = []
for line in lines:
    line = float(line)
    prices.append(line)

def avg_calculator(prices):
    return sum(prices)/len(prices)

def avg_calculator_5(prices):
    prices = prices[:5]
    return sum(prices)/len(prices)

print(f"5 days avg: {avg_calculator_5(prices)}")
print(f"total average: {avg_calculator(prices)}")
"""

#############################################################################################
# numbers = []
# total = 0
# count = 0
# #used chat to figure out reading a txt file
# with open("/workspaces/DATA_3500_sandbox/AAPL.2023.txt", "r") as file:
#     for line in file:
#             line = line.strip()
#             if line:  # avoid empty lines
#                 numbers.append(float(line))
# for number in numbers:
#      total+=number
#      count+=1
# print(f"average: ", total/count)
# total = count = 0
# for number in numbers:
#     total+=number
#     count+=1
#     if count == 5:
#          break
# print(f"average of first 5: ", total/count)

#############################################################################################

"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homweork.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""

file = open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/AAPL.2023.txt", "r")
lines = file.readlines()
prices = []

for line in lines:
    line = float(line)
    prices.append(line)

# print(lines)

def avg_calculator(list):
    return sum(list)/len(list)

#print average of first 4
print(f"avg of first 4: {avg_calculator(prices[:4])}")

#print average of last 4
print(f"avg of last 4: {avg_calculator(prices[-4:])}")

#start with 10,000 dollars
#4 day moving average
#loop through the list
#at each loop, calculate the average of the last four days (start at day 4)
#if the next day is greater than the average, we buy
#if the next day is lower than the average, we sell
#calculate profit/loss for that day and store in a variable

"""
i have a list of prices, i can loop through the list
each loop, i'll use the avg_calculator function to calculate the average of the last four days
"""
beg = 0
end = 4
profit = 0

for price in prices:
    if price > avg_calculator(prices[beg:end]):
        profit += price
        print(f"bought at {price} because it's greater than the 4 day avg:  {avg_calculator(prices[beg:end])}")
    else:
        profit -= price
        print(f"sold at {price} because it's less than the 4 day avg:  {avg_calculator(prices[beg:end])}")
    beg += 1
    end += 1
print(f"profit: {profit}")