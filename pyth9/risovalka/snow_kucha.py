def kucha_snega():
    import simple_draw as sd
    sd.resolution = (1200, 600)
    for i in range(30):
        y = sd.random_number(50, 100)
        x = sd.random_number(50, 300)
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=sd.random_number(10, 100))
