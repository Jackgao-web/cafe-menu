import tkinter as tk
from tkinter import messagebox

# Defining the menu items
menu_items = [
    ("Pizza", 12.99),
    ("Burger", 8.99),
    ("Hotdog", 5.99),
    ("Fries", 3.99),
    ("Soda", 2.99)
]

# Initializing the order total
order_total = 0

# Initializing the account dictionary
accounts = {"1": "1"}

# Function for adding the item to the order
def add_to_order(price, order_total_label):
    # Accessing the global variable
    global order_total
    order_total += price
    order_total_label.config(text=f"Order Total: ${order_total:.2f}")

# Function for showing the menu
def show_menu():
    # Getting the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Checking if the username and password are correct
    if username in accounts and accounts[username] == password:
        # Removing the login widgets
        login_label.grid_remove()
        username_entry.grid_remove()
        password_entry.grid_remove()
        login_button.grid_remove()
        add_account_button.grid_remove()

        # Creating the order total label
        order_total_label = tk.Label(root, text="Order Total: $0.00")
        order_total_label.pack()

        # Creating the menu label
        menu_label = tk.Label(root, text="Menu:")
        menu_label.pack()

        # Creating the menu items
        menu_frame = tk.Frame(root)
        menu_frame.pack(pady=10)

        for item in menu_items:
            item_name = item[0]
            item_price = item[1]
            item_label = tk.Label(menu_frame, text=f"{item_name}: ${item_price:.2f}")
            item_label.pack(side=tk.LEFT, padx=10)

            # Creating the item button
            item_button = tk.Button(menu_frame, text="Add to Order", command=lambda price=item_price, order_total_label=order_total_label: add_to_order(price, order_total_label))
            item_button.pack(side=tk.LEFT, padx=10)

        # Creating the checkout button
        checkout_button = tk.Button(root, text="Checkout", command=lambda: show_message_box(order_total))
        checkout_button.pack()
    else:
        # Showing an error message if the username or password is incorrect
        messagebox.showerror(title="Login Error", message="Incorrect username or password. Please try again.")

def add_account():
    # Getting the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Adding the account to the dictionary
    accounts[username] = password

    # Showing a success message
    messagebox.showinfo(title="Account Added", message="Account successfully added.")

def show_message_box(order_total):
    # Showing a message box with the order total
    messagebox.showinfo(title="Order Total", message=f"Your order total is ${order_total:.2f}. Thank you for your order!")

# Creating the main window
root = tk.Tk()
root.title("User Login")

# Creating the login label
login_label = tk.Label(root, text="Please enter your username and password:")
login_label.grid(row=0, column=0, padx=5, pady=5)

# Creating the entry fields
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=0, padx=5, pady=5)

# Creating the login button
login_button = tk.Button(root, text="Login", command=show_menu)
login_button.grid(row=3, column=0, padx=5, pady=5)

# Creating the add account button
add_account_button = tk.Button(root, text="Add Account", command=add_account)
add_account_button.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
