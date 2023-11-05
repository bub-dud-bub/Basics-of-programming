class Mashina:
    def Fuel_sp(mas):
        return round(int(mas) / 30000, 2)

    def Time(way):
        return round(int(way) / 90, 2)

    def Cost(fuel, way):
        return round(fuel * int(way) * 50, 2)


class Bus:
    def Fuel_sp(mas):
        return round(int(mas) / 20000, 2)

    def Time(way):
        return round(int(way) / 80, 2)

    def Cost(fuel, way):
        return round(fuel * int(way) * 50, 2)

class Truck:
    def Fuel_sp(mas):
        return round(int(mas) / 10000, 2)

    def Time(way):
        return round(int(way) / 70, 2)

    def Cost(fuel, way):
        return round(fuel * int(way) * 50, 2)
