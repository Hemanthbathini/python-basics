# Author: Hemanth Bathini
# Date: 11/05/2024
# Description: Allows the user to specify multiple products and stores them in a list of SmartProduct objects.
# A calcTotal function is updated to iterate through the list of products and sum their total costs.
# Displays detailed order information and the total cost


from SmartProduct import SmartProduct


def calcTotal(products):
    total_cost = 0.0
    for product in products:
        total_cost += product.get_total_cost()
    return total_cost


def main():
    products = []
    num_products = int(input("How many products would you like to order? "))

    for i in range(num_products):
        name = input(f"Enter the name of product #{i + 1}: ")
        units = int(input(f"Enter the number of units for {name}: "))
        product_id = i + 1  # Create a unique ID for each product
        price = 9.99
        product = SmartProduct(product_id, name, units, price)
        products.append(product)

    print("\nOrder Summary:")
    for product in products:
        print(
            f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Units: {product.get_units()}, Price per unit: ${product.get_price():.2f}, Total cost: ${product.get_total_cost():.2f}")

    total_order_cost = calcTotal(products)
    print(f"\nTotal order cost: ${total_order_cost:.2f}")


if __name__ == "__main__":
    main()
