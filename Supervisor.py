# Author: Hemanth Bathini
# Date: 11/12/2024
# Description: Defines a Supervisor class that inherits from Employee, adds a level attribute,
# and overrides the pay calculation to include a level-based bonus.

from Employee import Employee

class Supervisor(Employee):
    def __init__(self, name, employee_id, pay_rate, level):
        super().__init__(name, employee_id, pay_rate)
        self.__level = level

    def calcPay(self, hours_worked):
        base_pay = hours_worked * self._pay_rate
        bonus = 1000.00 * self.__level
        return base_pay + bonus

    def get_level(self):
        return self.__level

    def set_level(self, level):
        if level > 0:
            self.__level = level
        else:
            print("Invalid level. Level should be a positive integer.")
