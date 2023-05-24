# cafe_app.py

# Define menu items and their prices
menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.99,
    "Salad": 4.99
}

# Define function to display menu and get user order
def get_user_order():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    order = {}
    while True:
        item = input("Enter food name (or 'finish' to finish): ")
        if item == "finish":
            break
        elif item not in menu:
            print("Invalid item.")
        else:
            quantity = input("Enter quantity: ")
            if quantity.isdigit():
                order[item] = int(quantity)
            else:
                print("Invalid quantity. Please enter a number.")
    return order

# Define function to calculate total price of order
def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

# Main program
print("Welcome to the Cafe Click and Collect App!")

user_order = get_user_order()
total = calculate_total(user_order)
print("Order details:")
for item, quantity in user_order.items():
    print(f"{item}: {quantity}")
print(f"Total: ${total:.2f}")
