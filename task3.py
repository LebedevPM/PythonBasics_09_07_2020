class Cell:

    def __init__(self, cell_count: int):
        self.cell_count = cell_count

    def __add__(self, other):
        new_cell_count = self.cell_count + other.cell_count
        return Cell(new_cell_count)

    def __sub__(self, other):
        if self.cell_count > other.cell_count:
            new_cell_count = self.cell_count - other.cell_count
            return Cell(new_cell_count)
        else:
            raise ValueError('Разность клеток не может быть меньше или равна нулю')

    def __mul__(self, other):
        new_cell_count = self.cell_count * other.cell_count
        return Cell(new_cell_count)

    def __truediv__(self, other):
        new_cell_count = self.cell_count // other.cell_count
        if new_cell_count:
            return Cell(new_cell_count)
        else:
            raise ValueError('Разность клеток не может быть меньше или равна нулю')

    def make_order(self, line_length: int) -> str:
        cells_string = ''
        i = 1
        j = 1
        while i <= self.cell_count:
            if j <= line_length:
                cells_string += '*'
                i += 1
                j += 1
            else:
                cells_string += '\n'
                j = 1
        return cells_string


cell1 = Cell(50)
cell2 = Cell(10)
cell3 = cell1 - cell2
print(cell3.cell_count)
cell3 = cell1 * cell2
print(cell3.cell_count)
cell3 = cell1 / cell2
print(cell3.cell_count)
cell3 = cell1 + cell2
print(cell3.cell_count)
print(cell1.make_order(8))
print()
print(cell2.make_order(3))
print()
print(cell3.make_order(10))
print()
print(1)
