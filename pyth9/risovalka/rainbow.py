def LGBT():
    import simple_draw as sd
    y = 140
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for i in range(len(rainbow_colors)):
        point = sd.get_point(575, y)
        sd.circle(center_position=point, radius=900, color=rainbow_colors[i], width=20)
        y -= 30
