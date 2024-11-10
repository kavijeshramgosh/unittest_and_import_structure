'''
Turns "Application/" into a package for function_import.py

Any scripts in Application/ can be imported using:
from Application import *

This will import everything within __all__ stored in this init file

note: ___init___.py is not designed to be run as a script so cannot be
run on its own and -will- throw up an error if run but thats ok
which is what confused me for a while

'''
# This lets us call the function directly instead of adding Second_script.Two_Func()
# Also means other functions are not imported which may be useful in some cases
from .Second_script import Two_Func

__all__ = [ "First_script" , "Two_Func" , "main_script" ]

# Only these 2 are needed since these are the only scripts in this directory

# Additionally First_script does not need to be imported separately in here 
# as __all__ makes it visbile within Application/ for importing

