# 0. Title

## Description

What I learned from the tasks:

* Why JavaScript programming is amazing
* How to manipulate JSON data
* How to use request and fetch API
* How to read and write a file using fs module

---

## General Requirements
* Allowed editors: vi, vim and emacs.
* All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc
* You are not allowed to use var

---

# Tasks

These are all the tasks of this project, the ones that are completed link to the corresponding files.

### [0. Readme](./0-readme.js)

* Write a script that reads and prints the content of a file.

	- The first argument is the file path
	- The content of the file must be read in utf-8
	- If an error occurred during the reading, print the error object

### [1. Write me](./1-writeme.js)

* Write a script that writes a string to a file.

	- The first argument is the file path
	- The second argument is the string to write
	- The content of the file must be written in utf-8
	- If an error occurred during while writing, print the error object

### [2. Status code](./2-statuscode.js)

* Write a script that display the status code of a GET request.

	- The first argument is the URL to request (GET)
	- The status code must be printed like this: code: <status code>
	- You must use the module request

### [3. Star wars movie title](./3-starwars_title.js)

* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

	- The first argument is the movie ID
	- You must use the [Star wars API](./https://swapi-api.hbtn.io/api/films/:id) with the endpoint https://swapi-api.hbtn.io/api/films/:id
	- You must use the module request

### [4. Star wars Wedge Antilles](./4-starwars_count.js)

* Write a script that prints the number of movies where the character “Wedge Antilles” is present.

	- The first argument is the API URL of the [Star wars API](https://swapi-api.hbtn.io/api/films/): https://swapi-api.hbtn.io/api/films/
	- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
	- You must use the module request

### [5. Loripsum](./5-request_store.js)

* Write a script that computes the number of tasks completed by user id.

	- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
	- Only print users with completed task
	- You must use the module request

### [6. How many completed?](./6-completed_tasks.js)

* Write a script that computes the number of tasks completed by user id.

	- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
	- Only print users with completed task
	- You must use the module request

### [7. Who was playing in this movie?](./100-starwars_characters.js)

* Write a script that prints all characters of a Star Wars movie:

	- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
	- Display one character name by line
	- You must use the [Star wars API](https://swapi-api.hbtn.io/)
	- You must use the module request

### [8. Right order](./101-starwars_characters.js)

* Write a script that prints all characters of a Star Wars movie:

	- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
	- Display one character name by line in the same order of the list “characters” in the /films/ response
	- You must use the [Star wars API](https://swapi-api.hbtn.io/)
	- You must use the module request


---

### Author
* **Dominic Samo** - (https://github.com/DominicSamoes)
