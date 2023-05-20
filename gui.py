# -*- coding: utf-8 -*-

# GUI Contact Management System
# Author: Wahyu Indra Pramadhana
# Based on code from: OpenAI ChatGPT (https://openai.com)

import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()

# Create a Treeview widget for the table
table = ttk.Treeview(window)
table["columns"] = ("name", "number")

# Format the columns
table.column("#0", width=0, stretch=tk.NO)
table.column("name", anchor=tk.W, width=150)
table.column("number", anchor=tk.W, width=150)

# Create table headings
table.heading("#0", text="", anchor=tk.W)
table.heading("name", text="Name", anchor=tk.W)
table.heading("number", text="Number", anchor=tk.W)

# Create a label widget for the title
title_label = tk.Label(window, text="Contact List", font=("Helvetica", 14, "bold"))
title_label.grid(row=0, columnspan=2, pady=10)

# Display the table
table.grid(row=1, columnspan=2, padx=10, pady=10)

# Create a button widget for clearing the table
clear_button = tk.Button(window, text="Clear")
clear_button.grid(row=2, columnspan=2, pady=10)

# Create a label widget for the search title
search_label = tk.Label(window, text="Search Contact", font=("Helvetica", 14, "bold"))
search_label.grid(row=3, columnspan=2, pady=5)

# Create a label widget for the search by name
search_entry_label = tk.Label(window, text="Search by Name:")
search_entry_label.grid(row=4, column=0, sticky=tk.E)

# Create an entry widget for the search by name
search_entry = tk.Entry(window)
search_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

# Create a button widget for searching
search_button = tk.Button(window, text="Search")
search_button.grid(row=5, columnspan=2, pady=10)

# Create a label widget for "Create new contact"
create_label = tk.Label(window, text="Create new contact", font=("Helvetica", 14, "bold"))
create_label.grid(row=6, columnspan=2, pady=5)

# Create a label widget for the new contact name
name_label = tk.Label(window, text="Name:")
name_label.grid(row=7, column=0, sticky=tk.E)

# Create an entry widget for the new contact name
name_entry = tk.Entry(window)
name_entry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

# Create a label widget for the new contact number
number_label = tk.Label(window, text="Number:")
number_label.grid(row=8, column=0, sticky=tk.E)

# Create an entry widget for the new contact number
number_entry = tk.Entry(window)
number_entry.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

# Create a button widget for creating a new contact
create_button = tk.Button(window, text="Create")
create_button.grid(row=9, columnspan=2, pady=10)

# Create a label widget for "Remove Contact"
remove_label = tk.Label(window, text="Remove Contact", font=("Helvetica", 14, "bold"))
remove_label.grid(row=10, columnspan=2, pady=5)

# Create a label widget for the remove by name
remove_entry_label = tk.Label(window, text="Remove by Name:")
remove_entry_label.grid(row=11, column=0, sticky=tk.E)

# Create an entry widget for the remove by name
remove_entry = tk.Entry(window)
remove_entry.grid(row=11, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

# Create a button widget for removing a contact
remove_button = tk.Button(window, text="Remove")
remove_button.grid(row=12, columnspan=2, pady=10)

# Column 1 expands to fill available space
window.columnconfigure(1, weight=1)