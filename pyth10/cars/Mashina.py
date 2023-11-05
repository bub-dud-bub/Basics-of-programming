def Fuel_sp(mas):
    return round(int(mas) / 30000, 2)

def Time(way):
    return round(int(way) / 90, 2)

def Cost(way, fuel):
    return round(fuel * int(way) * 50, 2)
