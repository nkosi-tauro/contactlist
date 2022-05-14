
<h1 align="center">Rubiks Contact List</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/nkosi-tauro/contactlist?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/nkosi-tauro/contactlist?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/nkosi-tauro/contactlist?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/nkosi-tauro/contactlist?color=56BEB8">

</p>


<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/nkosi-tauro" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Welcome to the Rubiks Contact List!  
This is a simple contact list GUI application with basic CRUD functionality built using python and tkinter. 
It allows the user to add, sort, edit, delete and search for contacts. There is no persistent storage, a dictionary is used to temporaliry store the contacts in Key(contact name) and Value(contact number) pairs.


## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [tKinter](https://www.tkinter.org/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Python 3.8+](https://www.python.org/) installed.  

Note : tKinter comes with Python 3.8+ by default. If you are using an older version of Python or if tkinter is not found, you need to install tKinter separately.

```bash
Linux: 
$ sudo apt-get install python3-tk

Mac:
$ python3 -m pip install tkinter

Windows: 
$ pip install tkinter
```


## :checkered_flag: Using the Application ##

<details>
<summary>Installing the application</summary>
<br>

```bash
# Clone this project
$ git clone https://github.com/nkosi-tauro/contactlist

# Access the project folder
$ cd contactlist

# Run the project in the terminal or use your favorite IDE
Linux/Mac:
$ python3 contactlist.py

Windows:
$ python contactlist.py
```
</details>
<br>

<details>
<summary>Adding New Contacts</summary>
<br>
<b>To Add a new contact</b> :

1. Enter value in the Contact Name and Contact Number fields at the top of the application window
2. Select the Add Contact button located next to the Contact Number field.
3. Accept the prompt to add the new contact by clicking the OK button when prompted or decline to add by clicking cancel.

![Menu](images/add.png)
</details>
<br>

<details>
<summary>Editing Contacts</summary>
<br>
<b>To Edit a contact</b> : (contact needs to be selected from the displayed list)

1. Select a contact from the displayed list
2. Edit the Contact Number Value using the Contact Number field.
3. Click the Edit Contact button.
4. Accept the prompt to edit the contact by clicking the OK button when prompted or decline to edit by clicking cancel.


</details>
<br>

<details>
<summary>Deleting Contacts</summary>
<br>
<b>To Delete a contact</b> : (contact needs to be selected from the displayed list)

1. Select a contact from the displayed list
2. Click the Remove Contact button.
3. Accept the prompt to delete the contact by clicking the OK button when prompted or decline to delete by clicking cancel.


</details>
<br>

<details>
<summary>Searching for Contacts</summary>
<br>
<b>To Search for a contact</b> : 

1. Enter a value in the Search field. (Needs to be the contact name (case sensitive))
2. Click the Search Button.
3. Accept the prompt to search the contact name by clicking the OK button when prompted or decline to search by clicking cancel.


</details>
<br>

<details>
<summary>Sorting Contacts</summary>
<br>
<b>To Sort the contacts</b> : (contacts will be sorted alphabetically)

1. Click the Sort Contacts button.
2. Accept the prompt to sort the contacts by clicking the OK button when prompted or decline to sort by clicking cancel.

</details>
<br>

<details>
<summary>Exiting The Application</summary>
<br>
<b>To Exit the application</b> : 

Exit the application by clicking the Exit Program button.

</details>




## 📸 Demo Image ##
![Menu](images/gui.an.png)


## :memo: License ##

This project is under license from Mozilla Public License. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/nkosi-tauro" target="_blank">Nkosilathi Tauro</a>

&#xa0;

<a href="#top">Back to top</a>
