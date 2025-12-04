# Author: Hemanth Bathini
# Date: 10/08/24
# Description: This Python program is a Laboratory Equipment Manager
# that allows users to manage a list of lab equipment
lab_equipment = []
MAX_EQUIPMENT = 5


def display_menu():
    print("\nLaboratory Equipment Manager")
    print("1. Add Equipment")
    print("2. Remove Equipment")
    print("3. Display Current Equipment")
    print("4. Leave the Laboratory Manager")


def add_equipment():
    if len(lab_equipment) >= MAX_EQUIPMENT:
        print(f"Cannot add more equipment. The laboratory can only store {MAX_EQUIPMENT} pieces of equipment.")
    else:
        equipment = input("Enter the name of the equipment to add: ")
        lab_equipment.append(equipment)
        print(f"{equipment} has been added to the laboratory.")


def remove_equipment():
    equipment = input("Enter the name of the equipment to remove: ")
    if equipment in lab_equipment:
        lab_equipment.remove(equipment)
        print(f"{equipment} has been removed from the laboratory.")
    else:
        print(f"{equipment} is not in the laboratory.")


def display_equipment():
    if lab_equipment:
        print("Current equipment in the laboratory:")
        for item in lab_equipment:
            print(f"- {item}")
    else:
        print("The laboratory has no equipment at the moment.")


# Main program loop
def main():
    while True:
        display_menu()  # Show the menu
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            remove_equipment()
        elif choice == "3":
            display_equipment()
        elif choice == "4":
            print("Goodbye! Enjoy your journey of discovery.")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid option. Please choose a valid menu option.")


# Run the program
if __name__ == "__main__":
    main()
