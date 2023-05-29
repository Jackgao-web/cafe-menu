#importing libraries

import tkinter as tk
from tkinter import messagebox
import datetime


# Dictionary to store accounts and passwords
accounts = {}

def add_account():
    
    def add_account_inside():
        # Retrieve the account name and password from the input fields
        user_name = new_username_entry.get()
        password = new_password_entry.get()
        # Check if the account name is already stored
        if user_name in accounts:
            messagebox.showerror("Error", "Account already exists!")
        else:
            # Add the new account to the dictionary
            accounts[user_name] = password
        
            # Save the accounts to the file
            save_data()
        
            # Display a success message
            messagebox.showinfo("Success", "Account added successfully!")
        
            # Clear the input fields
            new_username_entry.delete(0, tk.END)
            new_password_entry.delete(0, tk.END)

    # Create a new window for adding accounts
    add_account_window = tk.Toplevel()
    add_account_window.title('New Account')

    new_username_label = tk.Label(add_account_window, text='New Username:', font=('Helvetica', 12))
    new_username_label.grid(row=0, column=0, pady=5, padx=5, sticky='w')

    new_username_entry = tk.Entry(add_account_window, font=('Helvetica', 12))
    new_username_entry.grid(row=0, column=1, pady=5, padx=5)

    new_password_label = tk.Label(add_account_window, text='New Password:', font=('Helvetica', 12))
    new_password_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

    new_password_entry = tk.Entry(add_account_window, show='*', font=('Helvetica', 12))
    new_password_entry.grid(row=1, column=1, pady=5, padx=5)

    tk.Button(add_account_window, text='Add Account', font=('Helvetica', 12), command=add_account_inside).grid(row=2, column=0, columnspan=2, pady=10)

    
# Define a function to show the order page
def show_order_page():
    # Create the main GUI layout
    # Show frame 2 and hide frame 1
    login_window.pack_forget()
    main_frame.pack()

def show_frame1():
    # Show frame 1 and hide frame 2
    main_frame.pack_forget()
    login_window.pack()
    # Clear the input fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Dictionary to store accounts and passwords
current_user = ""

def check_credentials():
    # Retrieve the username and password from the input fields
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are valid
    if username in accounts and accounts[username] == password:
        global current_user
        current_user = username  # Store the current logged-in user

        messagebox.showinfo("Success", "Login successful!")
        # Close the login window
        # If successful, hide the login window
        # Show the order page
        show_order_page()

    else:
        messagebox.showerror("Error", "Invalid username or password!")

def save_data():
    # Save the account data to a file named "accounts.txt"
    with open("accounts.txt", "w") as f:
        # Iterate over the dictionary items (user_name, password)
        for user_name, password in accounts.items():
            # Write each account entry as "user_name:password" followed by a newline character
            f.write(f"{user_name}:{password}\n")

def load_data():
    try:
        # Attempt to open the "accounts.txt" file for reading
        with open("accounts.txt", "r") as f:
            # Iterate over each line in the file
            for line in f:
                # Remove leading/trailing whitespaces and split the line into user_name and password
                user_name, password = line.strip().split(":")
                # Store the user_name and password in the accounts dictionary
                accounts[user_name] = password
    except FileNotFoundError:
        # If the file is not found, no accounts are loaded
        pass

load_data()

def update_quantity(item, quantity_entry):
    # Get the new quantity value from the quantity entry widget
    new_quantity = int(quantity_entry.get())
    
    # Update the quantity of the item in the cart list
    cart_list[item] = new_quantity
    
    # Update the order display by calling the x_botton() function
    x_botton()

def x_botton():
    order_textbox.delete("1.0", tk.END)
    for item in sorted(cart_list):
        price = float(item.split()[-1])
        quantity = cart_list[item]

        # Create a delete button next to each item in the order list
        delete_button = tk.Button(order_textbox, text="x", font=("Arial", 10, "bold"), fg="white", bg="red", bd=0, command=lambda item=item: remove_from_cart(item))

        # Insert the item, quantity, and price into the order textbox, with the delete button next to it
        order_textbox.window_create("end", window=delete_button)
        order_textbox.insert(tk.END, " " + item + " x ")

        # Create a quantity entry for each item
        quantity_entry = tk.Entry(order_textbox, width=5, font=("Arial", 10))
        quantity_entry.insert(tk.END, str(quantity))
        quantity_entry.bind("<FocusOut>", lambda event, item=item: update_quantity(item, quantity_entry))
        order_textbox.window_create(tk.END, window=quantity_entry)

        order_textbox.insert(tk.END, " $" + "{:.2f}".format(price * quantity).rjust(10) + "\n")

    # Calculate the total price of all items in the cart
    total_price = sum([float(item.split()[-1]) * quantity for item, quantity in cart_list.items()])

    # Update the total price label
    total_price_label.config(text="Total Price: ${:.2f}".format(total_price))


# Define a function to handle adding items to the cart
def add_to_cart():
    # Get the index of the current selection
    selection = menu_listbox.curselection()

    # If an item is selected
    if selection:
        # Get the text of the selected item
        item = menu_listbox.get(selection)

        # Add the item to the cart and update the quantity
        cart_list[item] = cart_list.get(item, 0) + 1

        # Clear the order text box
        order_textbox.delete("1.0", tk.END)

        # Sort the items in the cart alphabetically and add them to the order text box
        x_botton()

# Define a function to remove an item from the cart list when clicked
def remove_from_cart(item):
    # Check if the item exists in the cart list
    if item in cart_list:
        # Remove the item from the cart list
        del cart_list[item]
    
    # Update the order list and total price label
    order_textbox.delete("1.0", tk.END)
    x_botton()

def bill():
    items = ""
    total_price = sum([float(item.split()[-1]) * quantity for item, quantity in cart_list.items()])
    for item, quantity in cart_list.items():
        # Create a string representation of the item and its quantity
        items += item + " x " + str(quantity) + "\n"

    # Display a message box with the total bill amount and item details
    messagebox.showinfo("Total Bill Amount", f"Items:\n{items}\nTotal Bill Amount: $ {total_price:.2f}")

    # Get the current date and time
    current_datetime = datetime.datetime.now()
    # Create a filename based on the current date
    filename = current_datetime.strftime("%Y-%m-%d") + ".txt"

    # Write the sales details to the file
    with open(filename, "a") as f:
        f.write(f"Date and Time: {current_datetime}\n")
        f.write(f"User: {current_user}\n")  # Include the current logged-in user
        f.write(f"Items:\n{items}\n")
        f.write(f"Total Bill Amount: $ {total_price:.2f}\n")
        f.write("-" * 30 + "\n")

    # Show the login frame to return to the login page
    show_frame1()


#login page

# Create a new tk object to work with
root = tk.Tk()

# Create the login window
login_window = tk.Frame(root)

login_image = tk.PhotoImage(file="bdsc.png")
login_image_label = tk.Label(login_window, image=login_image)
login_image_label.grid(row=0, column=1)


# Add the username and password labels and entry fields
username_label = tk.Label(login_window, text='Username:', font=('Helvetica', 12))
username_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

username_entry = tk.Entry(login_window, font=('Helvetica', 12))
username_entry.grid(row=1, column=1, pady=5, padx=5)

password_label = tk.Label(login_window, text='Password:', font=('Helvetica', 12))
password_label.grid(row=2, column=0, pady=5, padx=5, sticky='w')

password_entry = tk.Entry(login_window, show='*', font=('Helvetica', 12))
password_entry.grid(row=2, column=1, pady=5, padx=5)

# Add the login button
tk.Button(login_window, text='Add Account', font=('Helvetica', 12), command=add_account).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(login_window, text='Login', font=('Helvetica', 12), command=check_credentials).grid(row=3, column=0, columnspan=2, pady=10)

# frame2
# Create a list to store the menu, each element contains the dish and price item
menu = [("Fries", 5.00),
        ("Burger", 2.50),
        ("Coke", 1.50),
        ("Pizza", 6.00),
        ("Fried Shrimp", 8.00),
        ("Pizza", 12.30),
        ("Jason's bbq", 16,00),
        ("Coffee", 3.00),]

# Create the main GUI layout
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

order_frame = tk.Frame(main_frame, bg='white', width=300)
order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

menu_frame = tk.Frame(main_frame, bg='white')
menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Menu Interface
menu_label = tk.Label(menu_frame, text='Menu', font=('Arial', 16), bg='white')
menu_label.pack(pady=20, padx=10, anchor='nw')

# Create a scrollbar for the menu
menu_scrollbar = tk.Scrollbar(menu_frame)
menu_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the menu list and display the price information
menu_listbox = tk.Listbox(menu_frame, height=20, width=40, font=('Arial', 12), yscrollcommand=menu_scrollbar.set)
menu_listbox.pack(side=tk.LEFT, padx=10, pady=20, fill=tk.BOTH, expand=True)

# Add dishes and prices to the list box
for item in menu:
    menu_listbox.insert(tk.END, item[0].ljust(20) + '{:.2f}'.format(item[1]).rjust(10))

# Set the default selection of the menu_listbox to the first item
menu_listbox.selection_set(0)

# Display selected order content on the right
order_label = tk.Label(order_frame, text='Selected Orders', font=('Arial', 16), bg='white')
order_label.pack(pady=20, padx=10, anchor='nw')

# Show the selected order in the text box
order_textbox = tk.Text(order_frame, height=20, width=50, font=('Arial', 12))
order_textbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Add and remove buttons
add_button = tk.Button(order_frame, text='Add', font=('Arial', 14, 'bold'), fg='white', bg='green', bd=0, command=add_to_cart)
add_button.pack(pady=10)

remove_button = tk.Button(order_frame, text="Remove", font=("Arial", 14, "bold"), fg="white", bg="red", bd=0, command=lambda: remove_from_cart(cart_list.clear()))
remove_button.pack(pady=10)

# Calculate the total price
total_price_label = tk.Label(order_frame, text='Total Price: $0.00', font=('Arial', 14), bg='white')
total_price_label.pack(pady=10, padx=10, anchor='se')

# Complete order button
complete_button = tk.Button(order_frame, text="Complete Order", font=("Arial", 14, "bold"), bg="blue", fg="white", bd=0, command=bill)
complete_button.pack(pady=10)

cart_list = {}

show_frame1()

root.mainloop()