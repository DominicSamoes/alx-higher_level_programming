# 0x0A. Python - Inheritance

## Description

Tasks on .

What I learned from the tasks:

* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions

---

## General Requirements
* Allowed editors: vi, vim and emacs.
* All files were created and compiled on Ubuntu 20.04.4 LTS using using python3 (version 3.8.5)
* All files end with a new line
* The first line of all files is exactly #!/usr/bin/python3
* Code style used is pycodestyle (version 2.8.*)
* All files executable
* The length of your files will be tested using wc
---

# Tasks

These are all the tasks of this project, the ones that are completed link to the corresponding files.

### [0. Lookup](./0-lookup.py)
* Write a function that returns the list of available attributes and methods of an object:
  	- Prototype: def lookup(obj):
	- Returns a list object
	- You are not allowed to import any module

### [1. My list](./1-my_list.py)
* Write a class MyList that inherits from list:
	- Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
	- You can assume that all the elements of the list will be of type int
	- You are not allowed to import any module

### [2. Exact same object](./2-is_same_class.py)
* Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

	- Prototype: def is_same_class(obj, a_class):
	- You are not allowed to import any module

### [3. Same class or inherit from](./3-is_kind_of_class.py)
* Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

	- Prototype: def is_kind_of_class(obj, a_class):
	- You are not allowed to import any module

### [4. Only sub class of](./4-inherits_from.py)
* Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

	- Prototype: def inherits_from(obj, a_class):
	- You are not allowed to import any module
### [5. Geometry module](./5-base_geometry.py)
* Write an empty class BaseGeometry.

	- You are not allowed to import any module


### [6. Improve Geometry](./6-base_geometry.py)
* Write a class BaseGeometry (based on 5-base_geometry.py).

	- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
	- You are not allowed to import any module

### [7. Integer validator](./7-base_geometry.py)
* Write a class BaseGeometry (based on 6-base_geometry.py).

	- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
	- Public instance method: def integer_validator(self, name, value): that validates value:
		+ you can assume name is always a string
		+ if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
		+ if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
	- You are not allowed to import any module

### [8. Rectangle](./8-rectangle.py)
* Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

	- Instantiation with width and height: def __init__(self, width, height):
		+ width and height must be private. No getter or setter
		+ width and height must be positive integers, validated by integer_validator



---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
