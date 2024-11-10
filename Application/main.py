# Importing First_script and Two_func() using relative imports 
# __init__.py is *not* being utilised to import these two for main.py

import First_script #Importing whole of "First.py"
from Second_script import * #Importing all functions from "second.py"

First_script.One_Func() #Can call any function in First through First.
Two_Func() #Calling Two directly from Second (I think this lacks clarity of where it has come from)


#Importing from a script in a different directory (using __init__.py)
from package import * #Importing using init file in packages

Third_script.Three_Func() #Imports all of "Third_script.py" but only runs Three_Func
Four_Func() #Only Four_Func is imported in __init__.py file in "package" folder




#Importing from a script in a different subdirectory (using __init__.py in main package)
from package.subpackage import * #Importing using init file in subpackages 

Fifth_script.Five_Func() #Imports all of "Fifth_script.py" but runs just Five_Func
Six_Func() #Only Six_Func imported through __init__.py file in "subpackages" folder  
