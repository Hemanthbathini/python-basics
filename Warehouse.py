# Author: Hemanth Bathini
# Date: 11/05/2024
# Description: The Warehouse class is initialized with an initial_goods parameter and provides methods to add,
# remove, and check the total number of goods.


class Warehouse:
    def __init__(self, initial_goods):
        self.__total_goods = initial_goods

    def add_goods(self):
        try:
            amount = int(input("Enter the number of goods to add: "))
            self.__total_goods += amount
            print(f"{amount} goods added. Total now: {self.__total_goods}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def remove_goods(self):
        try:
            amount = int(input("Enter the number of goods to remove: "))
            if amount <= self.__total_goods:
                self.__total_goods -= amount
                print(f"{amount} goods removed. Total now: {self.__total_goods}")
            else:
                print("Error: Not enough goods to remove.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def get_total_goods(self):
        return self.__total_goods
