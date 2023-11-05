# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 0
i = 0
sd.resolution = (1200, 600)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# list_x = []
# list_y = []
# list_len = []
# list_x.append(sd.random_number(50, 1150))
# list_y.append(600)
# list_len.append(sd.random_number(10, 100))
# while True:
#     sd.clear_screen()
#     # TODO здесь ваш код
#     if i % 5 == 0:
#         list_x.append(sd.random_number(50, 1150))
#         list_y.append(600)
#         list_len.append(sd.random_number(10, 100))
#     NN = N
#     while N > 0:
#         if list_y[N] > 0:
#             point = sd.get_point(list_x[N], list_y[N])
#             sd.snowflake(center=point, length=list_len[N])
#             list_y[N] = list_y[N] - 10
#         N -= 1
#     N = NN
#     if i % 5 == 0:
#         N += 1
#     i += 1
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()
N = 0
i = 0
sd.resolution = (1200, 600)
list_x = []
list_y = []
list_len = []
list_x.append(sd.random_number(50, 1150))
list_y.append(615)
list_len.append(sd.random_number(10, 100))
while True:
    # TODO здесь ваш код
    if i % 5 == 0:
        list_x.append(sd.random_number(50, 1150))
        list_y.append(600)
        list_len.append(sd.random_number(10, 100))
    NN = N
    sd.start_drawing()
    while N > 0:
        if list_y[N] > 15:
            point = sd.get_point(list_x[N], list_y[N])
            sd.snowflake(center=point, length=list_len[N], color=sd.background_color)
            list_y[N] = list_y[N] - 15
            list_x[N] = list_x[N] + sd.random_number(-7, 7)
            point = sd.get_point(list_x[N], list_y[N])
            sd.snowflake(center=point, length=list_len[N])
        N -= 1
    N = NN
    if i % 5 == 0:
        N += 1
    i += 1
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()






# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
