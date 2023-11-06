# Todolist App - Django Rest API

### Introduction
This is a simple todolist API, with basic CRUD operations (check out the Angular 8 Client project here: <https://github.com/fernando-vpran/todo-angular8-client>)

### API Features
- `/api/todolist` 
	- retrieve all tasks using **GET**
	- create a new task using **POST** with body JSON `{ "name": "Task name" }`
	- delete all tasks using **DELETE**
<br>
- `/api/todolist/{id}` 
	- retrieve task data using **GET**
	- update task data using **PUT** with body JSON 
		`{ "name": "Updated task name", "done": (True | False) }`
	- delete task using **DELETE**
<br>
- `/api/status/{done|undone} ` 
	- retrieve tasks by status using **GET**
		- status "done" = `{ "done": True }`
		- status "undone" = `{ "done": False }`

### Requirements
- Check if **Python** is already installed: Run `python --version` in the terminal to check the current installed version
	- check the LTS version at <https://www.python.org/downloads/>
	- run the terminal and verify the current python version, ensuring it was successfully installed (if an error message shows up, try to reboot your pc):


- Check if **pip** is already installed: `python -m pip --version` 
	- in case it is not, see the installment instructions in the official documentation: <https://pip.pypa.io/en/stable/installation/>


- Install **Django**: `python -m pip install Django`
	- verify Django installation: `python -m django --version`


- Install **SQLite3** (optional)
	- download _sqlite-tools-win32-x86-****.zip_ : <https://www.sqlite.org/download.html>
	- Create a folder inside C:\Program Files named sqlite. Extract the downloaded zip and put all three binary files in this folder.
	- Search for the "System Properties" program, and select the "Advanced" tab, then "Enviromnment Variables"
	- Choose "Path" variable and add "C:\Program Files\sqlite" to the path.
	- Verify Installation: `sqlite3 --version`


### Set up a virtual environment and install all project dependencies
	cd ./todo-django-rest-api
	python -m venv env
	env\Scripts\activate
	python -m pip install -r requirements.txt

### Run the app
_* the default port is 8000, but you need to run it on port 8080 to connect with my Angular interface_

	python manage.py runserver 8080