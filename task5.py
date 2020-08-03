class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки. Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки. Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки. Маркер')


stationery1 = Stationery('Кисточка')
stationery1.draw()
pen1 = Pen('Шариковая ручка')
pen1.draw()
pencil1 = Pencil('Простой карандаш')
pencil1.draw()
handle1 = Handle('Фломастер')
handle1.draw()