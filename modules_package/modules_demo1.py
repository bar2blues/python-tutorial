"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
# import modules_external.car as car
from modules_external import car #import info for more expecific

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        car.info(make, model)

m = ModulesDemo()
# m.builtin_modules()
m.car_description()
