# Welcome to the Rubiks Phone Book.
import time

#Dictionary of contacts
# This will be used to store the contacts.
phonebook = {}
program_open = True

def add_contact(key, value) :
  """Adds a new contact to the phonebook.""" 
  phonebook[key] = value
  print(f"{key} has been added to the phonebook.\n")
  return phonebook

def search_contact(key) :
  """Searches for a contact in the phonebook."""
  return phonebook

def delete_contact(key) :
  """Deletes a contact from the phonebook."""
  phonebook.pop(key)
  return print(f"{key} has been deleted from the phonebook.\n")

def sort_contact() :
  """Sorts the contacts in the phonebook."""
  return phonebook


def display_contacts() :
  """Displays all contacts in the phonebook."""
  print("Rubicks Phone Book\n")
  if len(phonebook) == 0:
    return print('The phonebook is empty.\n')
  else:
    print("You have the following contacts in your phonebook:")
    print ("{:<10} {:<10}".format('NAME','NUMBER'))
    for key, value in phonebook.items():
      contact_number = value
      print ("{:<10} {:<10}".format(key, contact_number))

def contact_validation() :
  """Validate the contact name and number before they are entered into the phonebook."""
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
  """Checks if selected key/contact name to be exists in the phonebook."""
  contact_name = input('Enter the name of the contact: ')
  # check if contact name is in the phonebook and then either delete or search for the contact based on user choice
  if contact_name in phonebook and choice == 3:
    delete_contact(contact_name)
  elif contact_name in phonebook and choice == 2:
    search_contact(contact_name)
  else:
    print(f'The contact {contact_name} does not exist in the phonebook.\n')
  
  return contact_name

while program_open:
    #Main Program Menu
    print('Welcome to the Rubiks Phone Book.\n')
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
      print('Add a new contact to the phonebook.\n')
      # Validate the contact name and number before they are entered into the phonebook.
      contact_name, contact_number = contact_validation()
      add_contact(contact_name, contact_number)
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 2 :
      # Validate if the contact name to be searched for exists in the phonebook.
      contact_exists(choice)
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 3 :
      print('Delete a contact from the phonebook.\n')
      # Validate if the contact name to be deleted exists in the phonebook.
      contact_exists(choice)
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 4 :
      sort_contact()
      print("You will be returned to the main menu in 2 seconds.\n")
      time.sleep(2)

    elif choice == 5 :
      # Display all contacts in the phonebook.
      display_contacts()
      print("\nYou will be returned to the main menu in 4 seconds.\n")
      time.sleep(4)

    elif choice == 6 :
      # Exit the program
      program_open = False
      print('Thank you for using the Rubiks Phone Book.\n')
    else :
      print('Invalid choice. Try again.')
      
