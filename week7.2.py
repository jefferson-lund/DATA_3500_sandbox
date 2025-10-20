
import numpy

prices = [123 ,234, 345, 456]
np_prices = numpy.array(prices)
print(f"np_prices: {np_prices}")


arr = numpy.zeros(10)
print(f"arr: {arr}")


random_distribution = numpy.random.normal(0, 1, 5)
print(f"random_distribution {random_distribution}")

# shuffle array

arr = numpy.array([1, 2, 4, 5, 6, 7])
numpy.random.shuffle(arr)
print(f"arr: {arr}")