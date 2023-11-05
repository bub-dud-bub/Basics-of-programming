def sun():
    import simple_draw as sd
    sd.circle(sd.get_point(150, 500), 50, sd.COLOR_YELLOW, width = 0)
    sd.line(sd.get_point(100, 500), sd.get_point(50, 500), width = 4)
    sd.line(sd.get_point(125, 525), sd.get_point(75, 575), width = 4)
    sd.line(sd.get_point(150, 550), sd.get_point(150, 600), width = 4)
    sd.line(sd.get_point(175, 525), sd.get_point(225, 575), width = 4)
    sd.line(sd.get_point(200, 500), sd.get_point(250, 500), width = 4)
    sd.line(sd.get_point(175, 475), sd.get_point(225, 425), width = 4)
    sd.line(sd.get_point(150, 450), sd.get_point(150, 400), width = 4)
    sd.line(sd.get_point(125, 475), sd.get_point(75, 425), width = 4)
    sd.pause()
