# Importing First_script and Two_func() using relative imports 
# __init__.py is *not* being utilised to import these two for main.py
# We can do this because these scripts are in the same directory as main.py

import First_script # Importing all functions from "First_script.py"
from Second_script import * # Importing all functions from "Second_script.py"

First_script.One_Func() # Can call any function in First_script
Two_Func() # Calling Two_Func directly from Second_script
# (Though I think this reduces clarity of where it has come from)



# Importing from a script in a subdirectory (using __init__.py in package)
from package import * # Runs the __init__ file and imports everything in __all__

Third_script.Three_Func() # Just note all of "Third_script.py" has been imported
Four_Func() # Only Four_Func is imported due to __init__.py file in "package" folder



# Importing from a script in a subsubdirectory (using the __init__.py in subpackage)
from package.subpackage import * # Runs the __init__ file and imports everything in __all__

Fifth_script.Five_Func() # All of Fifth_script has been imported
Six_Func() # Only Six_Func imported through __init__.py file in "subpackages" folder  
