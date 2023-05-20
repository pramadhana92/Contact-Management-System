# -*- coding: utf-8 -*-

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class AddressBook:
    def __init__(self, contacts=[]):
        self.contacts = []

    def add_contact(self, name, number):
        self.contacts.append(Contact(name, number))

    def get_contact_index(self, name):
        # get index of contact name
        # if the contact is found the index will be 0 or higher
        # if the contact is not found the index will be -1
        # lower function used to make the search mode case-insensitive
        return next((i for i, item in enumerate(self.contacts) if item.name.lower() == name.lower()), -1)

    def remove_contact(self, name):
        index = self.get_contact_index(name)
        if index >= 0:
            del self.contacts[index]
            print("Contact '%s' removed" % name)
            return True
        else:
            print("Contact '%s' not found" % name)
            return False

    def search_contact(self, name):
        index = self.get_contact_index(name)
        if index >= 0:
            number = self.contacts[index].number
            print("Contact '%s' number: %s" % (name, number))
            return self.contacts[index]
        else:
            print("Contact '%s' not found" % name)
            return False