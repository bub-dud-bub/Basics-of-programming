#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
import district.central_street.house1.room1 as rm1
import district.central_street.house1.room2 as rm2
import district.central_street.house2.room1 as rm3
import district.central_street.house2.room2 as rm4
import district.soviet_street.house1.room1 as rm5
import district.soviet_street.house1.room2 as rm6
import district.soviet_street.house2.room1 as rm7
import district.soviet_street.house2.room2 as rm8
list = []
list.extend(rm1.folks)
list.extend(rm2.folks)
list.extend(rm3.folks)
list.extend(rm4.folks)
list.extend(rm5.folks)
list.extend(rm6.folks)
list.extend(rm7.folks)
list.extend(rm8.folks)
join = ", ".join(list)
print('На районе живут:', join)
