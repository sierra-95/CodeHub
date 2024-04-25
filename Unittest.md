--------UNITTEST---------

Command: `python3 -m unittest tests.<file to test>`

***********
NOTE BETTER
***********
- Run the command on `/project/`.
- When running the command, don't add the `.py` extension.
- To avoid errors, label the file as "tests".

======illustration==========
`project/models/car.py`
`project/tests/test_car.py`

$ cat tests_car.py
-------------------
from models.car import engine as e
<<<<<rest of the code>>>>>

=======Example===========
$ pwd
/projects/
$ ls
models
tests
$ python3 -m unittest tests.test_car
-----<output>-------
Ran 3 tests in 0.001s
OK
