# Welcome to the Rubiks Contact List Application.
import time

#Dictionary of contacts (contact name and contact number, key value pairs)
# This will be used to store the contacts.
contactlist = {}
program_open = True

def add_contact(key, value) :
  """Adds a new contact to the contactlist.""" 
  contactlist[key] = value
  print(f"The Contact Name: '{key}' and Contact Number: '{value}' have been added to the Contact List.\n")
  return contactlist

def search_contact(key) :
  """Searches for a contact in the contactlist."""
  number = contactlist[key]
  return print(f"The Contact Name: '{key}' and Contact Number: '{number}' have been found in the Contact List.\n")

def delete_contact(key) :
  """Deletes a contact from the contactlist."""
  contactlist.pop(key)
  return print(f"{key} has been deleted from the Contact List.\n")

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


def display_contacts() :
  """Displays all contacts in the contactlist."""
  print("Rubicks Phone Book\n")
  if len(contactlist) == 0:
    return print('The Contact List is empty.\n')
  else:
    doYouWantToSort = input('Do you want to sort the contacts alphabetically before displaying them? (y/n): ')
    if doYouWantToSort == 'y':
      sort_contacts()
    else:
      print("You have the following contacts in your Contact List:")
      print ("{:<10} {:<10}".format('NAME','NUMBER'))
      for key, value in contactlist.items():
        contact_number = value
        print ("{:<10} {:<10}".format(key, contact_number))

def contact_validation() :
  """Validate the contact name and number before they are entered into the contactlist."""
  # check if contact name is greater or equal to 5 characters
  isLongEnough = False
  # check if contact number is a number
  isNumber = False

  while not isLongEnough:
    contact_name = input('Enter the name of the contact: ')
    if len(contact_name) >= 5:
      isLongEnough = True
    else:
      print('The name must be at least 5 characters long.\n')
      
  while not isNumber:
    try :
      contact_number = int(input('Enter the contact number: '))
      isNumber = True
    except ValueError:
      print('The number must be a number.\n')

  return contact_name, contact_number

def contact_exists(choice) :
  """Checks if selected key/contact name to be exists in the contactlist."""
  contact_name = input('Enter the name of the contact: ')
  # check if contact name is in the contactlist and then either delete or search for the contact based on user choice
  if contact_name in contactlist and choice == 3:
    delete_contact(contact_name)
  elif contact_name in contactlist and choice == 2:
    search_contact(contact_name)
  else:
    print(f'The Contact Name: "{contact_name}" does not exist in the contactlist.\n')
  
  return contact_name

#Main Program Menu Loop
# The program will run until the user chooses to exit. (Option 6)
while program_open:
    print('Welcome to the Rubiks Contact List.\n')
    print('What would you like to do?\n')
    print('1. Add a new contact')
    print('2. Search a contact')
    print('3. Delete a contact')
    print('4. Sort contacts')
    print('5. Display all contacts')
    print('6. Quit the program')
    print('\n')
    choice = int(input('Enter your choice: '))

    if choice == 1 :
      print('Add a new contact to the contactlist.\n')
      # Validate the contact name and number before they are entered into the contactlist.
      contact_name, contact_number = contact_validation()
      add_contact(contact_name, contact_number)
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 2 :
      print('Search for a contact name from the contactlist.\n')
      # Validate if the contact name to be searched for exists in the contactlist.
      contact_exists(choice)
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 3 :
      print('Delete a contact from the contactlist.\n')
      # Validate if the contact name to be deleted exists in the contactlist.
      contact_exists(choice)
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 4 :
      sort_contacts()
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 5 :
      # Display all contacts in the contactlist.
      display_contacts()
      print("\nYou will be returned to the main menu in 4 seconds.\n")
      time.sleep(4)

    elif choice == 6 :
      # Exit the program
      program_open = False
      print('Thank you for using the Rubiks Contact List Application.\n')
    else :
      print('Invalid choice. Try again.')
      
