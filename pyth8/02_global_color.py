# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg

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





print('Выберите цвет:\n1 - красный\n2 - оранжевый\n3 - жёлтый\n4 - зелёный\n5 - голубой\n6 - синий\n7 - фиолетовый')
colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
color = int(input())
sd.resolution = (1200, 800)
point, angle, lenth = sd.get_point(300, 200), 120, 100
triangle(point, angle, lenth, colors[color - 1])

point, angle, lenth = sd.get_point(300, 600), 90, 105
square(point, angle, lenth, colors[color - 1])

point, angle, lenth = sd.get_point(900, 200), 72, 95
five_angles(point, angle, lenth, colors[color - 1])

point, angle, lenth = sd.get_point(900, 600), 60, 85
six_angles(point, angle, lenth, colors[color - 1])
sd.pause()
