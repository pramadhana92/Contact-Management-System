# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

from contact import Contact, AddressBook
import gui
from gui import table

# instantiate AddressBook
ab = AddressBook()

# insert sample data to ab object
ab.add_contact("Anto", "08123456789")
ab.add_contact("Budi", "02123456789")
ab.add_contact("Caca", "08111111111")

def empty_table():
    table.delete(*table.get_children())

def insert_data_to_table(contact):
    table.insert("", tk.END, values=(contact.name, contact.number))

def display_table():
    # this function will get data from ab object and display to the table
    # every time this function called we need to empty the table first to avoid flood of duplicate data
    empty_table()
    for contact in ab.contacts:
        insert_data_to_table(contact)

def warning_dialog(name):
    messagebox.showinfo("Warning", "Contact '%s' not found." % name)

def search_contact():
    name = gui.search_entry.get()
    contact = ab.search_contact(name)
    if contact:
        empty_table()
        insert_data_to_table(contact)
    else:
        warning_dialog(name)

def create_contact():
    name = gui.name_entry.get()
    number = gui.number_entry.get()
    ab.add_contact(name, number)
    display_table()

def remove_contact():
    name = gui.remove_entry.get()
    result = ab.remove_contact(name)
    if result:
        display_table()
    else:
        warning_dialog(name)

# link functions to gui
gui.clear_button.configure(command=display_table)
gui.search_button.configure(command=search_contact)
gui.create_button.configure(command=create_contact)
gui.remove_button.configure(command=remove_contact)

if __name__ == "__main__":
    display_table()
    gui.window.mainloop()