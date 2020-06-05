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
    pass


class FlightVehicle(Vehicle):  # Vehicle
    pass


class Starship(FlightVehicle):  # FlightVehicle
    pass


class GroundVehicle(Vehicle):  # Vehicle
    pass


class Airplane(FlightVehicle):  # FlightVehicle
    pass


class Car(GroundVehicle):  # GroundVehicle
    pass


class Motorcycle(GroundVehicle):  # GroundVehicle
    pass
