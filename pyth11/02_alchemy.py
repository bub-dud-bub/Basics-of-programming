# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:
    def __str__(self):
        return 'Вода'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
class Air:
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
class Fire:
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ground):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
class Ground:
    def __str__(self):
        return 'Земля'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
class Storm:
    def __str__(self):
        return 'Шторм'
class Lightning:
    def __str__(self):
        return 'Молния'
class Steam:
    def __str__(self):
        return 'Пар'
class Dirt:
    def __str__(self):
        return 'Грязь'
class Dust:
    def __str__(self):
        return 'Пыль'
class Lava:
    def __str__(self):
        return 'Лава'


elm1 = Water()
elm2 = Air()
elm3 = elm1 + elm2
print(elm1, '+', elm2, '=', elm3)
print(Water(), '+', Fire(), '=', Water() + Fire())

print(Water(), '+', Ground(), '=', Water() + Ground())
print(Fire(), '+', Air(), '=', Fire()  + Air() )
print(Air(), '+', Ground(), '=', Air() + Ground())
print(Fire(), '+', Ground(), '=', Fire() + Ground())
print(Fire(), '+', Fire(), '=', Fire() + Fire())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
