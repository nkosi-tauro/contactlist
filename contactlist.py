# Welcome to the Rubiks Contact List Application.
# The Tkinter package will be used to create the GUI.
from tkinter import * 
from tkinter import messagebox

rubkisApp = Tk()
rubkisApp.title('Rubiks Contact List')
rubkisApp.geometry('700x350')

# Dictionary to store the contactlist
contactlist_dictionary = {}

def display_contacts():
    contactlist.delete(0, END)
    for key, value in sorted(contactlist_dictionary.items()):
      contact_number = value
      contactlist.insert(END,"{:<10} {:<10}".format(key, contact_number))


def add_contact() :
  """Adds a new contact to the contactlist.""" 
  if contact_name.get() == '' or contact_number.get() == '':
    messagebox.showerror('Required Fields', 'Please Enter the Contact Name and Contact Number')
    return
  contactlist_dictionary[contact_name.get()] = contact_number.get()
  contactlist.delete(0, END)
  contactlist.insert(END, (contact_name.get(), contact_number.get()))
  messagebox.showinfo("Contact Added", f"The Contact Name: '{contact_name.get()}' and Contact Number: '{contact_number.get()}' have been added to the Contact List.\n")
  clear_contact_input()
  display_contacts()

def search_contact(key) :
  """Searches for a contact in the contactlist."""
  number = contactlist[key]
  return print(f"The Contact Name: '{key}' and Contact Number: '{number}' have been found in the Contact List.\n")

def delete_contact(key) :
  """Deletes a contact from the contactlist."""
  contactlist.pop(key)
  return print(f"{key} has been deleted from the Contact List.\n")

def edit_contact(key) :
  """Edits a contact in the contactlist."""
  isNumber = False
  while not isNumber:
    try :
      contact_number_update = int(input('Enter the updated contact number: '))
      isNumber = True
    except ValueError:
      print('The number must be a number.\n')
  contactlist.update({key : contact_number_update})
  print(f"The Contact Name: '{key}' has been edited with the new Contact Number: '{contact_number_update}'.\n")
  return contactlist

def sort_contacts() :
  """Sort the contacts in the contactlist by alpabetical order"""
  print("Rubicks Phone Book\n")
  if len(contactlist) == 0:
    return print('Cannot sort an empty Contact List.\n')
  else:
    print("Your contactlist has been sorted alphabeticaly :")
    print ("{:<10} {:<10}".format('NAME','NUMBER'))
    for key, value in sorted(contactlist.items()):
      contact_number = value
      print ("{:<10} {:<10}".format(key, contact_number))


def clear_contact_input():
    contact_name_entry.delete(0, END)
    contact_number_entry.delete(0, END)

# def display_contacts() :
#   """Displays all contacts in the contactlist."""
#   print("Rubicks Phone Book\n")
#   if len(contactlist) == 0:
#     return print('The Contact List is empty.\n')
#   else:
#     doYouWantToSort = input('Do you want to sort the contacts alphabetically before displaying them? (y/n): ')
#     if doYouWantToSort == 'y':
#       sort_contacts()
#     else:
#       print("You have the following contacts in your Contact List:")
#       print ("{:<10} {:<10}".format('NAME','NUMBER'))
#       for key, value in contactlist.items():
#         contact_number = value
#         print ("{:<10} {:<10}".format(key, contact_number))


# Input Variables and Style Definitions for the the GUI Layout
# contact_name
contact_name = StringVar()
contact_name_label = Label(rubkisApp, text='Contact Name', font=('bold', 14), pady=20)
contact_name_label.grid(row=0, column=0, sticky=W)
contact_name_entry = Entry(rubkisApp, textvariable=contact_name)
contact_name_entry.grid(row=0, column=1)

# contact_number
contact_number = StringVar()
contact_number_label = Label(rubkisApp, text='Contact Number', font=('bold', 14))
contact_number_label.grid(row=0, column=2, sticky=W)
contact_number_entry = Entry(rubkisApp, textvariable=contact_number)
contact_number_entry.grid(row=0, column=3)

# Search Box
search_text = StringVar()
search_label = Label(rubkisApp, text='Search Contact', font=('bold', 14))
search_label.grid(row=1, column=0, sticky=W)
search_entry = Entry(rubkisApp, textvariable=search_text)
search_entry.grid(row=1, column=1)

# Contact List (Listbox)
# The listbox will be used to display the contacts in the contactlist.
contactlist = Listbox(rubkisApp, height=8, width=50, border=0)
contactlist.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
# The scrollbar will be used to scroll the listbox should the contents start overflowing.
scrollbar = Scrollbar(rubkisApp)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
contactlist.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=contactlist.yview)
# Bind selected item 
# contactlist.bind('<<ListboxSelect>>', select_item)


# Action Buttons (Add, Search, Delete, Edit, Sort, Display)
add_btn = Button(rubkisApp, text='Add Contact', width=12, command=add_contact)
add_btn.grid(row=2, column=4)

search_btn = Button(rubkisApp, text='Search Contact', width=12, command=search_contact)
search_btn.grid(row=3, column=4)

remove_btn = Button(rubkisApp, text='Remove Contact', width=12, command=delete_contact)
remove_btn.grid(row=4, column=4)

edit_btn = Button(rubkisApp, text='Edit Contact', width=12, command=edit_contact)
edit_btn.grid(row=5, column=4)

sort_btn = Button(rubkisApp, text='Sort Contact', width=12, command=sort_contacts)
sort_btn.grid(row=6, column=4)

clear_btn = Button(rubkisApp, text='Clear Input', width=12)
clear_btn.grid(row=7, column=4)


# Start the tkinter program
rubkisApp.mainloop()
