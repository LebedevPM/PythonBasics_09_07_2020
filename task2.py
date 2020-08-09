from abc import ABC, abstractmethod


class Wear:

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Wear):

    def __init__(self, name: str, size: float):
        self.size = size
        self.name = name

    @property
    def tissue_consumption(self):
        return self.size / 6.5 * 0.5


class Costume(Wear):
    def __init__(self, name: str, height: float):
        self.height = height
        self.name = name

    @property
    def tissue_consumption(self):
        return self.height * 2 + 0.3


coat1 = Coat('coat001', 42)
print(coat1.name)
print(coat1.size)
print(coat1.tissue_consumption)
costume1 = Costume('coat001', 1.95)
print(costume1.name)
print(costume1.height)
print(costume1.tissue_consumption)
print(1)

