# Test functions for the Rubiks Contact List Application.
import time

#Dictionary of contacts (contact name and contact number, key value pairs)
# This will be used to store the contacts.
contactlist = {}
program_open = True

def add_contact(key, value) :
  """Adds a new contact to the contactlist.""" 
  contactlist[key] = value
  return contactlist

def delete_contact(key) :
  """Deletes a contact from the contactlist."""
  contactlist.pop(key)
  return contactlist
