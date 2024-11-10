'''
Unit test scripts are not run like normal scripts. Instead they are "discovered" using the command:

python -m unnittest discover -s path/to/testing_scripts/from/working_directory -p "*.py"

the * wildcard at the end can run multiple testing scripts simultaneously


You cannot import scripts relatively from your package into the testing script as this file is 
adjacent to the package. As in 

├── src/
│   └── your_package/
│       └── module1.py
│       └── module2.py
├── tests/
│   ├── test_module1.py
│   ├── test_module2.py

so we need to set up our scripts into importable packages using __init__.py. Once each directory in
our package has an __init__.py (set up correctly) we can now start unit testing. 
(See structure of "Application" within this repo where each folder has a __init__.py)

We can then change directory to the root of our package (here we would cd into /Application) and run 
our discover command:

(don't run this particular one, theres an exact example on line 34)
E.g., python -m unittest discover -s ../tests/ -p "*.py"

This will search for and run test scripts from the testing directory and apply it to the directory you
are in

I will put some example tests underneath

'''

import unittest
import First_script # We can import First_script straight away as we are in /Application on command line

'''
These tests below aren't actually useful tests, these are more of a proof of concept to show how to get 
the tests to run in the first place

Switch to the /Application directory, run: python -m unittest discover -s ../tests -p "testing_with_no_pyprojecttoml.py" 
in the command line. This command above runs all tests in this script. 

'''
#Checks if One_Func within First_script.py returns None (which it obviously does as it doesnt return anything)

class TestOneFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(First_script.One_Func(), None)



# The import is different for this particular function as the location is different to One_Func

from package import *

class TestThreeFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(Third_script.Three_Func(), None)



from package.subpackage import *

class TestFiveFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(Fifth_script.Five_Func(), None)

'''
You should have now seen 3 passed tests if the command was run properly
please message me if it fails and you think something is broken

'''