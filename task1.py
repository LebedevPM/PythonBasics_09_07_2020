class Matrix:

    def __init__(self, data: list):
        """
        Инициализация матрицы в виде списка числовых списков
        :param data: строки матрицы в виде списка числовых списков.
        Если строки матрицы разной длины, они будут дополнены нулями.
        """
        i = 0
        while i < len(data):
            while len(data[i]) != max(map(len, data)):
                data[i].append(0)
            i += 1
        self.data = data

    def __str__(self):
        result = ''
        for el in self.data:
            result = result + ' '.join(list(map(str, el)))
            result = f'{result}\n'
        return result

    def min(self, other):
        return self if len(self.data) < len(other.data) else other

    def max(self, other):
        return self if len(self.data) > len(other.data) else other

    def __add__(self, other):
        i = 0
        new_matrix = []
        while i < min(len(self.data), len(other.data)):
            new_matrix.append(list(self.max(other).data[i]))
            j = 0
            while j < min(len(self.data[i]), len(other.data[i])):
                new_matrix[i][j] += self.min(other).data[i][j]
                j += 1
            i += 1
        while i < max(len(self.data), len(other.data)):
            new_matrix.append(self.max(other).data[i])
            i += 1
        return Matrix(new_matrix)


matrix1 = Matrix([[1, 2, 3], [1, 2, 3, 4, 5], [1, 2, 3, 4]])
matrix2 = Matrix([[1, 2, 3, 4, 5], [1, 2], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4]])
print(matrix1)
print(matrix2)
matrix3 = matrix1 + matrix2
print(matrix3)
