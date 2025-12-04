# Author: Hemanth Bathini
# Date: 11/12/2024
# Description: Contains functions to manage employees, including listing information and
# calculating total payroll, and provides a main function to add employees interactively.

from Worker import Worker
from Supervisor import Supervisor


def calcTotalPay(employee_list):
    """
    Calculate the total pay for all employees in the list.
    Assume each employee has worked 40 hours.
    """
    total_pay = 0
    for employee in employee_list:
        total_pay += employee.calcPay(40)  # Each employee worked 40 hours
    return total_pay


def listEmployees(employee_list):
    """
    List all employees with appropriate labels, indicating their type
    and relevant information.
    """
    for employee in employee_list:
        if isinstance(employee, Worker):
            shift_type = "Day" if employee.get_shift() == 1 else "Night"
            print(f"Worker - Name: {employee.get_name()}, ID: {employee.get_employee_id()}, Shift: {shift_type}")
        elif isinstance(employee, Supervisor):
            print(
                f"Supervisor - Name: {employee.get_name()}, ID: {employee.get_employee_id()}, Level: {employee.get_level()}")
        else:
            print("Unknown employee type")


def main():
    """
    Main function to manage adding employees, listing them, and calculating total pay.
    """
    employee_list = []

    try:
        num_employees = int(input("Enter the number of employees you wish to add: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    for _ in range(num_employees):
        employee_type = input("Enter 'S' to add a Supervisor or 'W' to add a Worker: ").strip().upper()

        if employee_type == 'S':
            name = input("Enter supervisor's name: ")
            employee_id = input("Enter supervisor's ID: ")
            try:
                pay_rate = float(input("Enter supervisor's pay rate: "))
                level = int(input("Enter supervisor's level: "))
            except ValueError:
                print("Invalid input for pay rate or level. Please try again.")
                continue

            supervisor = Supervisor(name, employee_id, pay_rate, level)
            employee_list.append(supervisor)

        elif employee_type == 'W':
            name = input("Enter worker's name: ")
            employee_id = input("Enter worker's ID: ")
            try:
                pay_rate = float(input("Enter worker's pay rate: "))
                shift = int(input("Enter worker's shift (1 for day, 2 for night): "))
                if shift not in [1, 2]:
                    print("Invalid shift. Enter 1 for day shift or 2 for night shift.")
                    continue
            except ValueError:
                print("Invalid input for pay rate or shift. Please try again.")
                continue

            worker = Worker(name, employee_id, pay_rate, shift)
            employee_list.append(worker)

        else:
            print("Invalid selection. Please enter 'S' for Supervisor or 'W' for Worker.")
            continue

    # List all employees
    print("\nEmployee List:")
    listEmployees(employee_list)

    # Calculate total payroll
    total_pay = calcTotalPay(employee_list)
    print(f"\nTotal payroll for all employees: ${total_pay:.2f}")


if __name__ == "__main__":
    main()
