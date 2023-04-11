# Задание 2.
#
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class Road:
    def __init__(self, _length, _width):
        self._Road_length = _length
        self._Road_width = _width
    def mass(self):
        return self._Road_length * self._Road_width
class MassCount(Road):
    def __init__(self, _Road_length, _Road_width, volume):
        super().__init__(_Road_length, _Road_width)
        self.volume = volume

r = MassCount(25, 10000, 125)
print(r.mass())