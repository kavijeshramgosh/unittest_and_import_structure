'''
Unit test scripts are not run like normal scripts. Instead they are "discovered" using the command:

python -m unittest discover -v -s path/to/testing_scripts/from/working_directory -p "*.py"

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

Instead you can import your scripts directly from an installed package (using a pyproject.toml)
The benefit of this is you do not need to be in any specific directory to run the discover
command as long as the path to the tests is correct

python -m unittest discover -v -s path/to/tests/from/work_dir -p "*.py" can run multiple scripts

E.g., python -m unittest discover -v -s ../tests/ -p "main.py"

This will search for and run test scripts 

I will put some example tests underneath
'''

# run: python -m unittest discover -v -s <insert correct path to tests here> -p "testing_with_pyprojecttoml.py"
# if you are in the root directory of this repo the command is:
# python -m unittest discover -v -s ./tests -p "testing_with_pyprojecttoml.py"

import unittest
from Application import First_script #Imports the root application directory from installed package

class TestOneFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(First_script.One_Func(), 1)


from Application.package import Third_script

class TestThreeFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(Third_script.Three_Func(), 3)


from Application.package.subpackage import Fifth_script

class TestFiveFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(Fifth_script.Five_Func(), 5)

'''
You should have now seen 3 passed tests if the command was run properly

note: the only thing that has changed between this script and the one without pyproject.toml is less imports 
due to line 36 importing everything from __init__.py within "Application/"
if there are many scripts within the first directory and no pyproject.toml exists, each script will need to
be imported manually ( I think so at least...)

'''