""""
given a list of numbers and a number k, return whether any two numbers from the list add up to k
"""

#create list
#create two variables to add
#create var k
#loop through list
    #loop with focus on one number, check if it adds with all the others
#if var1 and var2 sum to k, return true
import random

lst = []
for i in range(100):
    lst.append(random.randint(1,100))
# print(lst)
num1 = 0
num2 = 0
k = 17

def find_the_target(lst, k):
    for i in lst:
        for j in lst:
            if i + j == k:
                found = True
                break
    return found

# print(find_the_target(lst, k))
    
mixed_data = [4, "hello", 5, 3.2, 'true', 'false', "world", 89]
nums = [item for item in mixed_data if isinstance(item, int) == True]
# print(nums)

words = ["racecar", "ratsliveonnoevilstar", "banana", "fart", "dood"]

pals = [pal for pal in words if pal == pal[::-1]]
# print(pals)

#homework 4
#another stock trader script

#what is the expression
#what are we looping through
#what is the iterator variables
#what is the condition?

print([round(float(line), 2) for line in open("/workspaces/DATA_3500_sandbox/AAPL.2023.txt").readlines()])