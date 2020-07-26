array = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 19, 17, 20, 2, 5, 9, 81, 100, 44]
result_array = [el for el in array if array.count(el) == 1]
print(result_array)