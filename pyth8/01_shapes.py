# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см results/exercise_01_shapes.jpg
#
# TODO здесь ваш код
# def triangle(point, angle, lenth):
#     angle2 = angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     return 0
#
# def square(point, angle, lenth):
#     angle2 = angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     return 0
#
# def five_angles(point, angle, lenth):
#     angle2 = angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     return 0
#
# def six_angles(point, angle, lenth):
#     angle2 = angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     point = vector.end_point
#     angle2 += angle
#     vector = sd.Vector(point, angle2, lenth, 2)
#     vector.draw()
#     return 0



def total(point, angle, lenth):
    vector = sd.Vector(point, angle, lenth, 2)
    vector.draw()
    return vector.end_point

def triangle(point, angle, lenth):
    angle2, point2 = angle, point
    for i in range(2):
        point = total(point, angle2, lenth)
        angle2 += angle
    total(point2, angle2 - 180, lenth)

def square(point, angle, lenth):
    angle2, point2 = angle, point
    for i in range(3):
        point = total(point, angle2, lenth)
        angle2 += angle
    total(point2, angle2 - 180, lenth)

def five_angles(point, angle, lenth):
    angle2, point2 = angle, point
    for i in range(4):
        point = total(point, angle2, lenth)
        angle2 += angle
    total(point2, angle2 - 180, lenth)

def six_angles(point, angle, lenth):
    angle2, point2 = angle, point
    for i in range(5):
        point = total(point, angle2, lenth)
        angle2 += angle
    total(point2, angle2 - 180, lenth)
#
#
#
#
#
#
sd.resolution = (1200, 800)
point, angle, lenth = sd.get_point(300, 200), 120, 100
triangle(point, angle, lenth)

point, angle, lenth = sd.get_point(300, 600), 90, 105
square(point, angle, lenth)

point, angle, lenth = sd.get_point(900, 200), 72, 95
five_angles(point, angle, lenth)

point, angle, lenth = sd.get_point(900, 600), 60, 85
six_angles(point, angle, lenth)








# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)






# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
