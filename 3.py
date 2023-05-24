# cafe_app_gui_with_login_no_vars.py

import tkinter as tk

# Define menu items and their prices
menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.99,
    "Salad": 4.99
}

# Define function to calculate total cost of order
def calculate_total(order):
    menu = {"Burger": 5.99, "Fries": 3.0, "Soda": 1.99, "Salad": 4.99}
    total = sum([menu[item] * quantity for item, quantity in order.items()])
    return total


# Define function to submit order and display total
def submit_order():
    order = {}
    for item, entry in item_entries.items():
        quantity = entry.get()
        if quantity:
            quantity = int(quantity)
        else:
            quantity = 0
        if quantity > 0:
            order[item] = quantity
        entry.delete(0, tk.END)
    total = calculate_total(order)
    total_label.config(text=f"Total: ${total:.2f}")


# Define function to handle login
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "1" and password == "1":
        login_frame.pack_forget()
        menu_frame.pack(side=tk.LEFT, padx=10)
        button_frame.pack(side=tk.LEFT, padx=10)
    else:
        login_error_label.config(text="Incorrect username or password")

# Create Tkinter window and widgets
root = tk.Tk()
root.title("Cafe Click and Collect App")

# Create login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=10)

username_label = tk.Label(login_frame, text="Username:")
username_label.pack(side=tk.LEFT)
username_entry = tk.Entry(login_frame)
username_entry.pack(side=tk.LEFT)

password_label = tk.Label(login_frame, text="Password:")
password_label.pack(side=tk.LEFT)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(side=tk.LEFT)

login_button = tk.Button(login_frame, text="Login", command=handle_login)
login_button.pack(side=tk.LEFT, padx=10)

login_error_label = tk.Label(login_frame, fg="red")
login_error_label.pack()

# Create menu frame
menu_frame = tk.Frame(root)

item_entries = {}
for item, price in menu.items():
    item_frame = tk.Frame(menu_frame)
    item_frame.pack(fill=tk.X, pady=5)
    item_label = tk.Label(item_frame, text=item, width=10)
    item_label.pack(side=tk.LEFT)
    price_label = tk.Label(item_frame, text=f"${price:.2f}", width=8)
    price_label.pack(side=tk.LEFT)
    entry = tk.Entry(item_frame, width=4)
    entry.pack(side=tk.RIGHT)
    item_entries[item] = entry

# Create button frame
button_frame = tk.Frame(root)

submit_button = tk.Button(button_frame, text="Submit Order", command=submit_order)
submit_button.pack(pady=5)

total_label = tk.Label(button_frame, text="Total: $0.00", font=("Arial", 16))
total_label.pack()

root.mainloop()
