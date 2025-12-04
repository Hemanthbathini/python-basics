
# Author: Hemanth Bathini
# Date: 11/12/2024
# Description: Defines a Worker class that inherits from Employee and
# adds a shift attribute with methods to handle day or night shifts.

from Employee import Employee

class Worker(Employee):
    def __init__(self, name, employee_id, pay_rate, shift):
        super().__init__(name, employee_id, pay_rate)
        self.__shift = shift

    def get_shift(self):
        return self.__shift

    def set_shift(self, shift):
        if shift in [1, 2]:
            self.__shift = shift
        else:
            print("Invalid shift. Use 1 for day shift or 2 for night shift.")
