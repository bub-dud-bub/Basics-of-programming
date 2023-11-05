# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
def total(point, angle, lenth, color):
    vector = sd.Vector(point, angle, lenth, 2)
    vector.draw(color)
    return vector.end_point

def triangle(point, angle, lenth, color):
    angle2, point2 = angle, point
    for i in range(2):
        point = total(point, angle2, lenth, color)
        angle2 += angle
    total(point2, angle2 - 180, lenth, color)

def square(point, angle, lenth, color):
    angle2, point2 = angle, point
    for i in range(3):
        point = total(point, angle2, lenth, color)
        angle2 += angle
    total(point2, angle2 - 180, lenth, color)

def five_angles(point, angle, lenth, color):
    angle2, point2 = angle, point
    for i in range(4):
        point = total(point, angle2, lenth, color)
        angle2 += angle
    total(point2, angle2 - 180, lenth, color)

def six_angles(point, angle, lenth, color):
    angle2, point2 = angle, point
    for i in range(5):
        point = total(point, angle2, lenth, color)
        angle2 += angle
    total(point2, angle2 - 180, lenth, color)

print('Выберите фигуру:\n1 - треугольник\n2 - квадрат\n3 - пятиугольник\n4 - шестиугольник')
select = int(input())
print('Выберите цвет:\n1 - красный\n2 - оранжевый\n3 - жёлтый\n4 - зелёный\n5 - голубой\n6 - синий\n7 - фиолетовый')
colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
color = int(input())
sd.resolution = (1200, 800)
if select == 1:
    point, angle, lenth = sd.get_point(600, 400), 120, 100
    triangle(point, angle, lenth, colors[color - 1])
elif select == 2:
    point, angle, lenth = sd.get_point(600, 400), 90, 105
    square(point, angle, lenth, colors[color - 1])
elif select == 3:
    point, angle, lenth = sd.get_point(600, 400), 72, 95
    five_angles(point, angle, lenth, colors[color - 1])
elif select == 4:
    point, angle, lenth = sd.get_point(600, 400), 60, 85
    six_angles(point, angle, lenth, colors[color - 1])
sd.pause()
sd.pause()
