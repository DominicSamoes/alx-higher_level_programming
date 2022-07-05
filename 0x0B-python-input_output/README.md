# 0x0B. Python - Input/Output

## Description

Tasks on .

What I learned from the tasks:

* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

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

### [0. Read file](./0-read_file.py)
* Write a function that reads a text file (UTF8) and prints it to stdout:

	- Prototype: def read_file(filename=""):
	- You must use the with statement
	- You don’t need to manage file permission or file doesn't exist exceptions.
	- You are not allowed to import any module

### [1. Write to a file](./1-write_file.py) 
* Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

	- Prototype: def write_file(filename="", text=""):
	- You must use the with statement
	- You don’t need to manage file permission exceptions.
	- Your function should create the file if doesn’t exist.
	- Your function should overwrite the content of the file if it already exists.
	- You are not allowed to import any module

### [2. Append to a file](./2-append_write.py)
* Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

	- Prototype: def append_write(filename="", text=""):
	- If the file doesn’t exist, it should be created
	- You must use the with statement
	- You don’t need to manage file permission or file doesn't exist exceptions.
	- You are not allowed to import any module

### [3. To JSON string](./3-to_json_string.py)
* Write a function that returns the JSON representation of an object (string):

	- Prototype: def to_json_string(my_obj):
	- You don’t need to manage exceptions if the object can’t be serialized.



---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
