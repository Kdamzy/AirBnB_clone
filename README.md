0x00. AirBnB clone - The console
================================

Execution
=========

Your shell should work like this in interactive mode:
----------------------------------------------------
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)

(hbnb) 

(hbnb) quit

$

Also in non-interactive mode:
-----------------------------
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
----------------------------------------
EOF  help  quit

(hbnb) 

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

Documented commands (type help <topic>):
----------------------------------------

EOF  help  quit
(hbnb) 
$

Unittest
========

All your files, classes, functions must be tested with unit tests
-----------------------------------------------------------------

python3 -m unittest discover tests