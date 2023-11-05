#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.
import my_burger as mb
print('Двойной чизбургер:')
mb.bulka1()
mb.mayonez()
mb.kotleta()
mb.cheese()
mb.kotleta()
mb.cheese()
mb.cucumber()
mb.tomato()
mb.bulka2()
# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингридиентов - создать соответствующие функции в модуле my_burger
print('\n"Колхозный бургер":')
mb.bulka1()
mb.meat()
mb.potato()
mb.tomato()
mb.salad()
mb.cucumber()
mb.onion()
mb.bulka2()
