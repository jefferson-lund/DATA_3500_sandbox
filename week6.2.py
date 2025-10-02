file = open("C:/Users/Jefferson/DATA_3500_Repos/Sandbox/test_prices.txt", "r")
lines = file.readlines()
prices = []

for line in lines:
    line = float(line)
    prices.append(line)

print(lines)

def avg_calculator(list):
    return sum(list)/len(list)

# #print average of first 4
print(f"avg of first 4: {avg_calculator(prices[:4])}")

#print average of last 4
print(f"avg of last 4: {avg_calculator(prices[-4:])}")


beg = 0
end = 4
profit = 0
money = 1000
position = 50

for price in prices[4:]:
    if price > avg_calculator(prices[beg:end]):
        if money > price:
            money -= price
            position += 1
            print(f"bought at {price} because it's greater than the 4 day avg:  {avg_calculator(prices[beg:end])}")
        else:
            print(f"not enough money to buy at {price}")
    else:
        if position > 0:
            money += price
            position -= 1
            print(f"sold at {price} because it's less than the 4 day avg:  {avg_calculator(prices[beg:end])}")
        else:
            print(f"no position to sell at {price}")
    beg += 1
    end += 1
    print("\n")
price = prices[-1]
print(f"money left over: {money}")
print(f"profit: {price*(position-50) + money - 1000} ({money/1000}%)")
