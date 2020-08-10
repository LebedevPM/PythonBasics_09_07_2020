class OfficeEquipment:
    """Офисная техника - родительский класс"""
    __equipment_types = ('printer', 'scanner', 'xerox')  # возможные типы устройств
    __manufacturers = ('Canon', 'Epson', 'HP', 'Samsung', 'Xerox')  # возможные производители
    __paper_sizes = ('A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6')  # возможные размеры бумаги

    def __init__(self,
                 equipment_type: str,
                 manufacturer: str,
                 name: str,
                 price: float,
                 size: int,
                 paper_size: str,
                 papers_per_min: int,
                 device_location: str
                 ):
        """
        :param equipment_type: тип оборудования
        :param manufacturer: производитель оборудования
        :param name: наименование оборудования
        :param price: цена оборудования
        :param size: размер оборудования в кубических сантиметрах
        :param paper_size: размер подходящей для работы оборудования бумаги
        :param papers_per_min: количество обрабатываемых листов в минуту
        :param device_location: расположение устройства, новое устройство может попасть только на склад
        """

        if equipment_type in OfficeEquipment.__equipment_types:
            self.equipment_type = equipment_type
        if manufacturer in OfficeEquipment.__manufacturers:
            self.manufacturer = manufacturer
        self.name = name
        self.price = price
        self.size = size
        if paper_size in OfficeEquipment.__paper_sizes:
            self.paper_size = paper_size
        self.papers_per_min = papers_per_min
        self.device_location = device_location


class Printer(OfficeEquipment):
    __printing_technologies = ('laser', 'LED', 'inkjet', 'thermal printing')

    def __init__(self,
                 manufacturer: str,
                 name: str,
                 price: float,
                 size: int,
                 paper_size: str,
                 papers_per_min: int,
                 printing_technology: str
                 ):
        """
        Инициализация параментров экземпляра класса Printer
        :param manufacturer: производитель принтера
        :param name: наименование принтера
        :param price: цена принтера
        :param size: размер принтера в кубических сантиметрах
        :param paper_size: размер подходящей для работы принтера бумаги
        :param papers_per_min: количество листов, обрабатываемых принтером в минуту
        :param printing_technology: технология печати принтера
        """

        if printing_technology in Printer.__printing_technologies:
            self.printing_technology = printing_technology
        super().__init__('printer', manufacturer, name, price, size, paper_size, papers_per_min, '')

    def __str__(self):
        return list(self)



class Scanner(OfficeEquipment):
    __scanner_types = ('flatbed', 'lingering', 'manual', 'slide scanner', 'camera')

    def __init__(self,
                 manufacturer: str,
                 name: str,
                 price: float,
                 size: int,
                 paper_size: str,
                 papers_per_min: int,
                 scanner_type: str
                 ):
        """
        Инициализация параментров экземпляра класса Scanner
        :param manufacturer: производитель сканера
        :param name: наименование сканера
        :param price: цена сканера
        :param size: размер сканера в кубических сантиметрах
        :param paper_size: размер подходящей для работы сканера бумаги
        :param papers_per_min: количество листов, обрабатываемых сканером в минуту
        :param scanner_type: тип сканера
        """
        if scanner_type in Scanner.__scanner_types:
            self.scanner_type = scanner_type
        super().__init__('scanner', manufacturer, name, price, size, paper_size, papers_per_min, '')


class Xerox(OfficeEquipment):

    def __init__(self,
                 manufacturer: str,
                 name: str,
                 price: float,
                 size: int,
                 paper_size: str,
                 papers_per_min: int,
                 ):
        """
        Инициализация параментров экземпляра класса Xerox
        :param manufacturer: производитель ксерокса
        :param name: наименование ксерокса
        :param price: цена ксерокса
        :param size: размер ксерокса в кубических сантиметрах
        :param paper_size: размер подходящей для работы ксерокса бумаги
        :param papers_per_min: количество листов, обрабатываемых ксероксом в минуту
        """
        super().__init__('xerox', manufacturer, name, price, size, paper_size, papers_per_min, '')


# техника в департаментах
office_equipment_at_department = {
    'dep1': [],
    'dep2': [],
    'dep3': []
}


class Warehouse:
    # техника на складе
    office_equipment_at_warehouse = {
        'printer': [],
        'scanner': [],
        'xerox': []
    }

    @staticmethod
    def take_to_warehouse(device: OfficeEquipment):
        if device.device_location == 'warehouse':
            print('Это устройство уже на складе')
        else:
            Warehouse.office_equipment_at_warehouse[device.equipment_type].append(device)
            device.device_location = 'warehouse'

    @staticmethod
    def send_from_warehouse(device: OfficeEquipment, department: str):
        if device.device_location == '':
            print('Новое устройство должно сначало отправиться на склад')
        elif device.device_location == department:
            print('Устройство уже находится в указанном департаменте')
        elif device.device_location in office_equipment_at_department.keys():
            print('Устройство между департаментами должно перемещаться через склад')
        else:
            pass


printer1 = Printer('HP', 'LaserJet Pro M15w', 7650, 10400, 'A4', 18, 'laser')
scanner1 = Scanner('Epson', 'Perfection V370 Photo', 10890, 8067, 'A4', 5, 'flatbed')
xerox1 = Xerox('Xerox', '3025BI', 2381, 7500, 'A3', 20)
Warehouse.take_to_warehouse(printer1)
