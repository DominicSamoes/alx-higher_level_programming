# 0x07. Python - Test-driven development

## Description

Tasks on .

What I learned from the tasks:

* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

---

## General Requirements
* Allowed editors: vi, vim and emacs.
* All files were created and compiled on Ubuntu 20.04.4 LTS using using python3 (version 3.8.5)
* All files end with a new line
* The first line of all files is exactly #!/usr/bin/python3
* Code style used is pycodestyle (version 2.8.*)
* All files executable
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

---

# Tasks

These are all the tasks of this project, the ones that are completed link to the corresponding files.

### [0. Integers addition](./0-add_integer.py)
* Write a function that adds 2 integers.
  	- Prototype: def add_integer(a, b=98):
	- a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
	- a and b must be first casted to integers if they are float
	- Returns an integer: the addition of a and b
	- You are not allowed to import any module

### [1. Divide a matrix](./2-matrix_divided.py)
* Write a function that divides all elements of a matrix.
	- Prototype: def matrix_divided(matrix, div):
	- matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
	- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
	- div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
	- div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
	- All elements of the matrix should be divided by div, rounded to 2 decimal places
	- Returns a new matrix
	- You are not allowed to import any module

### [2. Say my name](./3-say_my_name.py)
* Write a function that prints My name is <first name> <last name>
	- Prototype: def say_my_name(first_name, last_name=""):
	- first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
	- You are not allowed to import any module



---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
