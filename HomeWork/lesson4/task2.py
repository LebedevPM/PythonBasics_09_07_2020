array = [300, -20, 2, 12, 44, 1, -1, 1, 4, -22, -17, 10, 7, -60, 1, 78, -52, 123, 55]
print(array)
result_array = [el for idx, el in enumerate(array) if idx and el > array[idx - 1]]
print(result_array)