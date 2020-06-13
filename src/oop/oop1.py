# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    def __init__(self, name, brand):
        self.name = name,
        self.branch = branch
        

class GroundVehicle(Vehicle):
    def __init__(self, name, brand, make, year):
        super().__init__(make, brand)
        self.passenger: make
        self.wheels: year


class Car(GroundVehicle):
    def __init__(self, name, brand, make, year):
        super().__init__(name, brand, make, year, wheels)
        self.wheels=wheels


class Motorcycle(GroundVehicle):
    def __init__(self, name, brand, make, year, some_attribute):
        super.__init__(name, brand, make, year)
        self.some_attribute = some_attribute
    

class FlightVehicle(Vehicle):
    def __init__(self, name, brand, capacity, air_property):
        super().__init__(name, brand)
        self.capacity=capacity
        self.air_property: air_property


class Airplane(FlightVehicle):
    def __init__(self, name, brand, capacity, airproperty, year):
        super.__init__(name, brand, capacity, airproperty)
        self.year = year



class Starship(FlightVehicle):
    def __init__(self, name, brand, capacity, airproperty, vaporPower):
        super.__init__(name, brand, capacity, airproperty)
        self.vaporPower = vaporPower
        


        


