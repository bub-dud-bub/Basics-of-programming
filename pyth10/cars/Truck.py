def Fuel_sp(mas):
    return round(int(mas) / 10000, 2)

def Time(way):
    return round(int(way) / 70, 2)

def Cost(way, fuel):
    return round(fuel * int(way) * 50, 2)
