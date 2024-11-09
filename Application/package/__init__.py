'''
Turns "package" into a package for main.py

___init___.py is not designed to be run as a script so cannot be run on its own
'''

from .Fourth_script import Four_Func #This lets us call the function directly instead of adding Fourth.Four

__all__ = ["Third_script","Four_Func"]#Third in the table lets us call Third.Three directly

#Only these 2 are needed in __all__ as these are the only scripts in this directory