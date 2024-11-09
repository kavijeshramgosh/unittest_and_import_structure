'''
This is how you can import things from Application in the same directory as Application
'''

from Application import *

First_script.One_Func()

Two_Func()

from Application.package import *

Third_script.Three_Func()

Four_Func()

from Application.package.subpackage import *

Fifth_script.Five_Func()

Six_Func()
