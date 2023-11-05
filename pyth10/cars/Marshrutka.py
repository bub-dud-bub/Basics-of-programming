def Fuel_sp(mas):
    return round(int(mas) / 20000, 2)

def Time(way):
    return round(int(way) / 80, 2)

def Cost(way, fuel):
    return round(fuel * int(way) * 50, 2)
