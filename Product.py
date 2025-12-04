# Author: Hemanth Bathini
# Date: 11/05/2024
# Description: Product.py defines the Product class with private variables.
# It has getter and setter methods for each attribute


class Product:
    def __init__(self):
        self.__name = ""
        self.__units = 0
        self.__price = 0.0
        self.__total_cost = 0.0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_total_cost(self):
        return self.__total_cost

    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost
