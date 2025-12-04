# Author: Hemanth Bathini
# Date: 11/05/2024
# Description: The main function presents a simple menu and interacts with the Warehouse object to add/remove goods and output the total stock.
# The loop continues until the user selects the quit option.




from Warehouse import Warehouse

def main():
    warehouse = Warehouse(0)  # Start with 0 goods
    while True:
        print("\nWarehouse Menu:")
        print("1. Add Goods")
        print("2. Remove Goods")
        print("3. Output Total")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            warehouse.add_goods()
        elif choice == "2":
            warehouse.remove_goods()
        elif choice == "3":
            print(f"Total goods in warehouse: {warehouse.get_total_goods()}")
        elif choice == "4":
            print("Exiting the warehouse manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
