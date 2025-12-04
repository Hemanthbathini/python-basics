# Author: Hemanth Bathini
# Date: 11/05/2024
# Description: Prompts the user for product details. Sets the price to 9.99.
# Uses calcTotal to calculate the total order cost and displays the final order summary.


from Product import Product

def calcTotal(product):
    total_cost = product.get_units() * product.get_price()
    product.set_total_cost(total_cost)

def main():
    product = Product()

    name = input("Enter the product name: ")
    product.set_name(name)

    units = int(input("Enter the number of units you want to order: "))
    product.set_units(units)

    product.set_price(9.99)

    calcTotal(product)

    print(f"\nOrder Summary:")
    print(f"Product: {product.get_name()}")
    print(f"Units: {product.get_units()}")
    print(f"Price per unit: ${product.get_price():.2f}")
    print(f"Total cost: ${product.get_total_cost():.2f}")

if __name__ == "__main__":
    main()
