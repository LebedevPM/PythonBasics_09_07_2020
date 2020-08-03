class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.position = position
        super().__init__(name, surname, wage, bonus)

    def get_full_name(self):
        return f'{self.surname} {self.name}'


worker1 = Position('John', 'Smith', 'Manager', 100000, 25000)
print(worker1.get_full_name())
print(worker1.get_total_income())