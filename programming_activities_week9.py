"""
Activity 1

Write a python program that creates a list of all even nymbers from 2 to 100 using list comprehension
"""

list = [num for num in range(2,101) if num%2==0]
print(f"list: {list}")