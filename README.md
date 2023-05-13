AirBnB Clone - The Console
================================
![image](https://github.com/IB01Manuel/AirBnB_clone/assets/117752150/223f9bb7-801b-4dc8-a7af-ca87ae5ac9c2)

Description
=============
This team project is part of the ALX School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

The purpose of this project is to understand how to:
======================================================
create a Python package.
create a command interpreter using the cmd module.
serialize and deserialize a Class.
write and read a JSON file.
manage datetime.
use *args and **kwargs
handle named arguments in a function
HTML and CSS concepts.

Before developing a big and complex web application, we will build the frontend step-by-step. “design” / “sketch” / “prototype” each element:
================================================================================
Create simple HTML static pages
Style guide
Fake contents
No Javascript
No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Objectives
=====================
What is HTML
How to create an HTML page
What is a markup language
What is the DOM
What is an element / tag
What is an attribute
How does the browser load a webpage
What is CSS
How to add style to an element
What is a class
What is a selector
How to compute CSS Specificity Value
What are Box properties in CSS

Requirements
===============
PYTHON SCRIPT REQUIREMENTS
allowed editors: vi, vim, emacs
the first line of all files should be exactly #!/usr/bin/python3
all code should use the PEP8 style (version 1.7.*)
all files must be executable
all files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
PYTHON TEST CASE REQUIREMENTS
all test files should be in the folder tests
all test files should be text files (extension: .txt)
all test files should be executed using the command python3 -m doctest ./tests/*
all modules should have documentation python3 -c 'print(__import__("my_module").__doc__)'
all functions (inside and outside of classes) should have documentation python3 -c 'print(__import__("my_module").my_funct\ ion.__doc__)'

General
========

Allowed editors: vi, vim, emacs
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be W3C compliant and validate with W3C-Validator
All your CSS files should be in styles folder
All your images should be in images folder
You are not allowed to use !important and id (#... in the CSS file)
You are not allowed to use tags img, embed and iframe
You are not allowed to use Javascript
Current screenshots have been done on Chrome 56 or more.
No cross browsers
You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots
Usage Examples for console
Interactive Mode
~/me$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
~/me$
Non-Interactive Mode
~/me$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

~/me$ cat test_help
help
~/me$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
~/me$
Bugs
At this time, there are no known bugs.

License
========
AirBnB Clone is open source and free to download and use

File storage
=============
The folder engine manages the serialization and deserialization of all the data, following a JSON format.

A FileStorage class is defined in file_storage.py with methods to follow this flow: <object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>

The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

Tests
========  
All the code is tested with the unittest module. The test for the classes are in the test_models folder.

Authors
=======
. Ibibo Manuel ~ (https://github.com/IB01Manuel): 
. Victor Stephen ~ (https://github.com/victorstephen26):

  ![image](https://github.com/IB01Manuel/AirBnB_clone/assets/117752150/585833f2-dbbc-4653-b307-7160e9343a01)
