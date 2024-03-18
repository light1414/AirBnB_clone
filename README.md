AirBnB_clone - The console.

Overview of the Project

As the first ALX project on a full web application, the project's objective is to launch a basic clone of the AirBnB website. The AirBnB objects will be managed by the command interpreter.

This project contains several tasks:

creating a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
creating all classes used for AirBnB (User, State, City, Place, Amenities, Reviews) that inherit from BaseModel
creating the first abstracted storage engine of the project: File storage.
creating all unittests to validate all our classes and storage engine

Learning Objectives

Creating a Python package

How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it

Handling named arguments in a function

Files
HBNHCommand: console.py
Amenity: models/amenity.py
BaseModel: models/base_model.py
City: models/city.py
models.init : models/init.py
Place: models/place.py
Review: models/review.py
State: models/state.py
User: models/user.py
FileStorage: models/engine/file_storage.py
engine.init: models/engine/init.py

How the command intepreter manages the AirBnB Objects
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
All tests must pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

console

AUTHORS:
Daniel Osakwe - [dantata49@gmail.com]
