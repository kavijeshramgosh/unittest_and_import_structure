'''
You cannot import scripts relatively from Applications here as it adjacent to Application
E.g., Technically not in the same directory

Instead you can import only if you install the Applications package (through a project.toml)

Alternatively, you can test by cd /Applications and running the following command:

python -m unnittest discover -s path/2/tests/from/work_dir -p "*.py" can run multiple scripts

E.g., python -m unittest discover -s ../Tests_folder/ -p "main.py"

This will search for and run Test scripts from elsewhere in directory you are in which
is useful before you have setup packages

I will put some example tests underneath
'''

import unittest
import First_script

class TestOneFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(First_script.One_Func(), None)

#In Application directory, run 'python -m unittest discover -s ../tests_folder -p "test*' in CLI

from package import *

class TestThreeFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(Third_script.Three_Func(), None)

#Same command as above also runs this script but the import is different

from package.subpackage import *

class TestFiveFunction(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(Fifth_script.Five_Func(), None)

        