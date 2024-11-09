'''
Turns "subpackage" into a package for main.py

___init___.py is not designed to be run as a script so cannot be run
'''

from .Sixth_script import Six_Func

__all__ = ["Fifth_script","Six_Func"]

#Only these 2 are needed since these are the only scripts in this directory
