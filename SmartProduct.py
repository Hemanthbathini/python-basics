# Author: Hemanth Bathini
# Date: 11/05/2024
# Description: Constructor now takes product_id, name, units, and price as parameters.
# Calculates the total cost in the constructor.
# Getter and setter methods are provided for each attribute


class SmartProduct:
    def __init__(self, product_id, name, units, price):
        self.__product_id = product_id
        self.__name = name
        self.__units = units
        self.__price = price
        self.__total_cost = self.__units * self.__price

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

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
