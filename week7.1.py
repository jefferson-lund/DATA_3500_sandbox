"""
divide without divide:

take denominator and add to itself as many times as needed to reach numerator
number of times run is the quotient
"""


def division(numerator, denominator):
    quotient = 0
    counter = 0
    while counter < numerator:
        counter += denominator
        quotient += 1    
    return(quotient)


# print(f"answer: {division(72,3)}")

file = open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/test.txt", "w")

names = ["Jacob", '\n', "Mary\n", "Steven\n", "Erick\n", "Amy\n"]

# print(names)
file.writelines(names)
file.close()

file = open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/test.txt", "r")
names_2 = file.readlines()
file.close()


#read in number.txt and get mean, stdev, etc
import statistics
with open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/numbers.txt") as number_file:
    lines = number_file.readlines()
    numbers = []

    for line in lines:
        numbers.append(int(line))

stdev = statistics.stdev(numbers)
mean = statistics.mean(numbers)

with open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/test.txt", "w") as file:
    file.write(f"Mean: {mean}\n")
    file.write(f"Standard Deviation: {stdev}\n")

