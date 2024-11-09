'''
Turns "Application" into a package for Tests.py

___init___.py is not designed to be run as a script so cannot be run
'''

from .Second_script import Two_Func

__all__ = ["First_script","Two_Func"]

#only these 2 are needed since these are the only scripts in this directory

