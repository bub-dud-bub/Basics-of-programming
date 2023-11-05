# -*- coding: utf-8 -*-

import simple_draw as sd
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    pass
    def __init__(self, x_cord, y_cord):
            self.x = x_cord
            self.y = y_cord
            self.len = sd.random_number(10, 100)
    def clear_previous_picture(self):
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(center=self.point, length=self.len, color=sd.background_color)
    def move(self):
        self.y -= 10
        self.point = sd.get_point(self.x, self.y)
        return self.y
    def draw(self):
        sd.snowflake(center=self.point, length=self.len)
    def get_fallen_flakes(self):
        if self.y < 0:
            self.clear_previous_picture()
            self.y = sd.random_number(500, 700)
            self.x = sd.random_number(50, 550)
            self.len = sd.random_number(10, 100)

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
def get_flakes(count):
    flakes = []
    for i in range (0, count):
        flakes.append(Snowflake(sd.random_number(50, 550), sd.random_number(500, 700)))
    return flakes


def append_flakes(flakes, count):
    flakes.insert(count, Snowflake(sd.random_number(50, 550), sd.random_number(500, 700)))

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
N = 1
flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.get_fallen_flakes()# подчитать сколько снежинок уже упало
    if N <= 10:
        append_flakes(flakes, N)
        N += 1
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
