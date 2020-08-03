class Road:
    __asphalt_mass = 100

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_mass(self, thickness=5):
        mass = self._length * self._width * self.__asphalt_mass * thickness
        return mass


highway = Road(500, 30)
print(f'На постройку дороги потребуется {highway.road_mass(10)} кг асфальта')
