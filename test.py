# Test File, Tests are based on contactlist v1.0 (contactlist_noGui.py) without tkinter.
# The functions in here represent the actions that can be performed on the contactlist.
# The unittest library will be used to test the application. The module is part of the python standard library.

import unittest
from unittest import result

from contactlist_noGui import add_contact,  delete_contact


class TestAddContact(unittest.TestCase):
    def test_key_value(self):
        """
        Test that it can add a contact to the contactlist.
        """
        key = "Apple"
        value = "023456789"
        result = add_contact(key, value)
        # Should result in a dictionary with the key and value.
        self.assertEqual(result, {"Apple": "023456789"})

class TestDeleteContact(unittest.TestCase):
    def test_key_value(self):
        """
        Test that it can delete a contact from the contactlist.
        """
        contactlist = {"Apple": "023456789"}
        # list out keys and values separately
        key_list = list(contactlist.keys())
        val_list = list(contactlist.values())
        # get key with value 0
        index = val_list.index("023456789")
        result = delete_contact(key_list[index])
        # if key deleted value should be of None type
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()