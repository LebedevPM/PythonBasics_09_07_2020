import random


class Car:
    def __init__(self, name: str, color: str):
        """
        :param name: Марка и модель автомобиля
        :param color: Цвет автомобиля
        :param is_police: Является автомобиль полицеским
        Speed - Скорость нового экземпляра всегда равна 0
        """
        self.name = name
        self.color = color
        self.is_police = False
        self.speed = 0

    def go(self):
        """Пускает автомобиль в движение, задавая ему случайную скорость от 20 км/ч до 120 км/ч.
        Также можно использовать для изменения скорости автомобиля на другое рандомное значение
        """
        if not self.speed:
            print(f'Автомобиль {self.name} {self.color} поехал')
        else:
            print(f'Автомобиль {self.name} {self.color} изменил скорость')
        self.speed = random.randint(20, 100)

    def stop(self):
        """Останавливает автомобиль - делает скорость автомобиля равной 0"""
        self.speed = 0
        print(f'Автомобиль {self.name} {self.color} остановлен')

    def turn(self, direction: str):
        """
        Поворачивает автомобиль в указанном направлении
        :param direction: Направление, в котором должен продолжить движение автомобиль
        """
        if direction.lower() == 'left':
            print(f'Автомобиль {self.name} {self.color} повернул налево')
        elif direction.lower() == 'right':
            print(f'Автомобиль {self.name} {self.color} повернул направо')
        elif direction.lower() == 'back':
            print(f'Автомобиль {self.name} {self.color} развернулся')
        else:
            print('ОШИБКА: Автомобиль может поворачивать только налево, направо или назад')

    def show_speed(self):
        if self.speed:
            print(f'Текущая скорость автомобиля {self.name} {self.color} составляет {self.speed}')
        else:
            print(f'Автомобиль {self.name} {self.color} стоит на месте')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} {self.color} превысил скорость на  {self.speed - 60} км/ч')
        elif self.speed:
            print(f'Текущая скорость автомобиля {self.name} {self.color} составляет {self.speed}')
        else:
            print(f'Автомобиль {self.name} {self.color} стоит на месте')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} {self.color} превысил скорость на  {self.speed - 40} км/ч')
        elif self.speed:
            print(f'Текущая скорость автомобиля {self.name} {self.color} составляет {self.speed}')
        else:
            print(f'Автомобиль {self.name} {self.color} стоит на месте')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name: str, color: str):
        self.is_police = True
        super().__init__(name, color)


town_car = TownCar('Nissan X-Trail', 'Metallic')
town_car.go()
town_car.show_speed()
town_car.turn('right')
town_car.turn('back')
town_car.turn('left')
town_car.go()
town_car.show_speed()
town_car.stop()
town_car.show_speed()

work_car = WorkCar('Lexus GS 350', 'Black')
work_car.go()
work_car.show_speed()
work_car.turn('right')
work_car.turn('back')
work_car.turn('left')
work_car.go()
work_car.show_speed()
work_car.stop()
work_car.show_speed()

sport_car = SportCar('Ferrari LaFerrari', 'Red')
sport_car.go()
sport_car.show_speed()
sport_car.turn('right')
sport_car.turn('back')
sport_car.turn('left')
sport_car.go()
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()

police_car = PoliceCar('LADA Vesta Sport', 'Metallic')
police_car.go()
police_car.show_speed()
police_car.turn('right')
police_car.turn('back')
police_car.turn('left')
police_car.go()
police_car.show_speed()
police_car.stop()
police_car.show_speed()
