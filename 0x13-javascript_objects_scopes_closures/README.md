# 0. Title

## Description

What I learned from the tasks:

* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What this means
* What undefined means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

---

## General Requirements
* Allowed editors: vi, vim and emacs.
* All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc
---

# Tasks

These are all the tasks of this project, the ones that are completed link to the corresponding files.

### [0. Rectangle #0](./0-rectangle.js)

* Write an empty class Rectangle that defines a rectangle:
	- You must use the class notation for defining your class

### [1. Rectangle #1](./1-rectangle.js)

* Write a class Rectangle that defines a rectangle:

	- You must use the class notation for defining your class
	- The constructor must take 2 arguments w and h
	- Initialize the instance attribute width with the value of w
	- Initialize the instance attribute height with the value of h

### [2. Rectangle #2](./2-rectangle.js)

* Write a class Rectangle that defines a rectangle:

        - You must use the class notation for defining your class
        - The constructor must take 2 arguments w and h
        - Initialize the instance attribute width with the value of w
        - Initialize the instance attribute height with the value of h
	- If w or h is equal to 0 or not a positive integer, create an empty object

### [3. Rectangle #3](./3-rectangle.js)

* Write a class Rectangle that defines a rectangle:

        - You must use the class notation for defining your class
        - The constructor must take 2 arguments w and h
        - Initialize the instance attribute width with the value of w
        - Initialize the instance attribute height with the value of h
        - If w or h is equal to 0 or not a positive integer, create an empty object
	- Create an instance method called print() that prints the rectangle using the character X


### [4. Rectangle #4](./4-rectangle.js)

* Write a class Rectangle that defines a rectangle:

        - You must use the class notation for defining your class
        - The constructor must take 2 arguments w and h
        - Initialize the instance attribute width with the value of w
        - Initialize the instance attribute height with the value of h
        - If w or h is equal to 0 or not a positive integer, create an empty object
        - Create an instance method called print() that prints the rectangle using the character X
	- Create an instance method called rotate() that exchanges the width and the height of the rectangle
	- Create an instance method called double() that multiples the width and the height of the rectangle by 2

### [5. Square #0](./5-square.js)

* Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

	- You must use the class notation for defining your class and extends
	- The constructor must take 1 argument: size
	- The constructor of Rectangle must be called (by using super())

### [6. Square #1](./6-square.js)

* Write a class Square that defines a square and inherits from Rectangle of 5-square.js:

        - You must use the class notation for defining your class and extends
	- Create an instance method called charPrint(c) that prints the rectangle using the character c
		+ If c is undefined, use the character X

### [7. Occurrences](./7-occurrences.js)

* Write a function that returns the number of occurrences in a list:

	- Prototype: exports.nbOccurences = function (list, searchElement)

### [8. Esrever](./8-esrever.js)

* Write a function that returns the reversed version of a list:

	- Prototype: exports.esrever = function (list)
	- You are not allow to use the built-in method reverse

### [9. Log me](./9-logme.js)

* Write a function that prints the number of arguments already printed and the new argument value. (see example below)

	- Prototype: exports.logMe = function (item)
	- Output format: <number arguments already printed>: <current argument value>

### [10. Number conversion](./10-converter.js)

* Write a function that converts a number from base 10 to another base passed as argument:

	- Prototype: exports.converter = function (base)
	- You are not allowed to import any file
	- You are not allowed to declare any new variable (var, let, etc..)

### [11. Factor index](./100-map.js)

* Write a script that imports an array and computes a new array.

	- Your script must import list from the file 100-data.js
	- You must use a map. 
	- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
	- Print both the initial list and the new list




---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
