import simple_draw as sd
def rozha():
    x, y, color = 900, 225, sd.COLOR_RED
    start_point = sd.get_point(x, y)
    sd.circle(start_point, 45, color, width = 1)
    sd.line(sd.get_point(x-20, y-20), sd.get_point(x+20, y-20), color, 1)
    sd.line(sd.get_point(x-20, y+17), sd.get_point(x-10, y+5), color, 1)
    sd.line(sd.get_point(x-10, y+17), sd.get_point(x-20, y+5), color, 1)
    sd.line(sd.get_point(x+20, y+17), sd.get_point(x+10, y+5), color, 1)
    sd.line(sd.get_point(x+10, y+17), sd.get_point(x+20, y+5), color, 1)

    sd.line(sd.get_point(900, 180), sd.get_point(900, 90), color, 1)
    sd.line(sd.get_point(900, 160), sd.get_point(860, 145), color, 1)
    sd.line(sd.get_point(900, 160), sd.get_point(940, 145), color, 1)
    sd.line(sd.get_point(900, 90), sd.get_point(860, 50), color, 1)
    sd.line(sd.get_point(900, 90), sd.get_point(940, 50), color, 1)

    sd.line(sd.get_point(900, 322), sd.get_point(900, 270), sd.COLOR_YELLOW, 1)
