# 0x06. Python - Classes and Objects

## Description

Tasks on .

What I learned from the tasks:

* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the __dict__ of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the getattr function


---

## General Requirements
* Allowed editors: vi, vim and emacs.
* All files were created and compiled on Ubuntu 20.04.4 LTS using using python3 (version 3.8.5)
* All files end with a new line
* The first line of all files is exactly #!/usr/bin/python3
* Code style used is pycodestyle (version 2.8.*)
* All files executable
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
---

# Tasks

These are all the tasks of this project, the ones that are completed link to the corresponding files.

### [0. My first square](./0-square.py)
* Write an empty class Square that defines a square:
  - You are not allowed to import any module

### [1. Square with size](./1-square.py)
* Write a class Square that defines a square by: (based on 0-square.py)
	- Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
* Why?
	- Why size is private attribute?
		+ The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. 

### [2. Size validation](./2-square.py)
* Write a class Square that defines a square by: (based on 1-square.py)
	- Private instance attribute: size
	- Instantiation with optional size: def __init__(self, size=0):
		+ size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
		+ if size is less than 0, raise a ValueError exception with the message size must be >= 0
	- You are not allowed to import any module

### [3. Area of a square](./3-square.py)
* Write a class Square that defines a square by: (based on 2-square.py)
	- Private instance attribute: size
	- Instantiation with optional size: def __init__(self, size=0):
		+ size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
                + if size is less than 0, raise a ValueError exception with the message size must be >= 0
		+ Public instance method: def area(self): that returns the current square area
        - You are not allowed to import any module


### [4. Access and update private attribute](./4-square.py)
* Write a class Square that defines a square by: (based on 3-square.py)
	- Private instance attribute: size:
		+ property def size(self): to retrieve it
		+ property setter def size(self, value): to set it:
			_ size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
			_ if size is less than 0, raise a ValueError exception with the message size must be >= 0
	- Instantiation with optional size: def __init__(self, size=0):
	- Public instance method: def area(self): that returns the current square area
	- You are not allowed to import any module
* Why?
	- Why a getter and setter?
		+ Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.



---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
