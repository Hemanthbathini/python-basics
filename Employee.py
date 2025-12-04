# Author: Hemanth Bathini
# Date: 11/12/2024
# Description:  Defines a base Employee class to store general employee data, calculate pay,
# and provide getter/setter methods for its attributes.


class Employee:
    def __init__(self, name, employee_id, pay_rate):
        self._name = name
        self._employee_id = employee_id
        self._pay_rate = pay_rate

    def calcPay(self, hours_worked):
        return hours_worked * self._pay_rate

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def get_pay_rate(self):
        return self._pay_rate

    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate
