import simple_draw as sd
def halupa():
    step = 375
    sd.resolution = (1400, 600)
    sd.rectangle(sd.get_point(0, 0), sd.get_point(1400, 25), color = sd.COLOR_GREEN, width=0)
    sd.rectangle(sd.get_point(375, 25), sd.get_point(750, 225), color = sd.COLOR_RED, width=1)
    for y in range(25, 225, 25):
        y1 = y + 25
        if y % 50 == 0: step -= 25
        else: step += 25
        for x in range(step, 725, 50):
            x1 = x + 50
            point = sd.get_point(x, y)
            point1 = sd.get_point(x1, y1)
            sd.rectangle(point, point1, color = sd.COLOR_RED, width=1)
    x, y, x1, y1 = 365, 225, 759, 225
    while (x != x1):
        sd.line(sd.get_point(x, y), sd.get_point(x1, y1), sd.COLOR_ORANGE, width=1)
        x += 1
        x1 -= 1
        y += 1
        y1 += 1
