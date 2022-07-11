# 0x0C. Python - Almost a circle

## Description

What I learned from the tasks:

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

## General Requirements
* Allowed editors: vi, vim and emacs.
* All files were created and compiled on Ubuntu 20.04.4 LTS using using python3 (version 3.8.5)
* All files end with a new line
* The first line of all files is exactly #!/usr/bin/python3
* Code style used is pycodestyle (version 2.8.*)
* All files executable

---

# Tasks

These are all the tasks of this project, the ones that are completed link to the corresponding files.

### [0. If it's not tested it doesn't work](./tests/)
* 
  - All your files, classes and methods must be unit tested and be PEP 8 validated.

### [1. Base class](./models/base.py)
* Write the first class Base:

* Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

* Create a file named models/base.py:

	- Class Base:
		+ private class attribute __nb_objects = 0
		+ class constructor: def __init__(self, id=None)::
			_ if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
			_ otherwise, increment __nb_objects and assign the new value to the public instance attribute id
* This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)


---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
