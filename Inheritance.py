class Vehicle:
    def __init__(self, Brand, milege):
        self.Brand = Brand
        self.milege = milege

    def show_details(self):
        print("The brand of vehicle is : ", self.Brand)
        print("The milege of vehicle is :", self.milege)


class Bike(Vehicle):
    def __init__(self, Brand, milege, color, cost):
        super().__init__(Brand, milege)
        self.color = color
        self.cost = cost

    def show_bike(self):
        print("The color of bike is : ", self.color)
        print("The cost of bike is  : ", self.cost)

b=Bike("Avenger","50 km/hr","Black",125000)

b.show_details()

b.show_bike()
