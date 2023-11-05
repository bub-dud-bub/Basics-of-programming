# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.good_job = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            self.shopping()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        if self.good_job == True:
            self.house.money += 150
        else:
            self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            self.work()

    def cat_shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачьей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            self.work()

    def cleaning(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('{} убрался в доме'.format(self.name), color='magenta')

    def new_job(self):
        self.good_job = True
        cprint('{} устроился на хорошую работу'.format(self.name), color='green')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_a_cat(self, house, cat):
        cprint('{} подобрал кота'.format(self.name), color='cyan')
        cat.cat_appeared(house=my_sweet_home)
    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.cat_food <= 10:
            self.cat_shopping()
        elif self.house.money < 100:
            self.work()
        elif self.house.dirt >= 100:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def cat_appeared(self, house):
        self.house = house
        cprint('У {} появился дом'.format(self.name), color='cyan')
    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def scratch(self):
        cprint('{} драл всё что можно'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5

    def sleep(self):
        cprint('{} спал как убитый'.format(self.name), color='green')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.scratch()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 0
        self.money = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьей еды осталось {}, денег осталось {}, уровень грязи: {}'.format(
            self.food, self.cat_food, self.money, self.dirt)


citizens = [
    Man(name='Никита'),
    Cat(name='Лев'),
    Man(name='Ростислав'),
    Cat(name='Тигр')
]

my_sweet_home = House()
for i in range(len(citizens)):
    if isinstance(citizens[i], Man):
        citizens[i].go_to_the_house(house=my_sweet_home)
        citizens[i].pick_up_a_cat(house=my_sweet_home, cat=citizens[i+1])
        citizens[i].new_job()

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
