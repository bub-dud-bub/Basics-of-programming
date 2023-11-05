def drevo():
    def draw_branches(point, angle, length):
        if length < 15:
            return 0
        branch1 = sd.Vector(point, angle + 30, length)
        branch1.draw(sd.COLOR_GREEN)
        draw_branches(branch1.end_point, branch1.angle, length * 0.75)
        branch2 = sd.Vector(point, angle - 30, length)
        branch2.draw(sd.COLOR_GREEN)
        draw_branches(branch2.end_point, branch2.angle, length * 0.75)
        return 0
    import simple_draw as sd
    vector = sd.Vector(sd.get_point(1050, 25), 90, 175)
    vector.draw()
    point, angle, length = sd.get_point(1050, 200), 90, 100
    draw_branches(point, angle, length)
