from functools import reduce

array = [el for el in list(range(100, 1001)) if el % 2 == 0]
print(array)
composition = reduce(lambda x, y: x * y, array)
print(composition)