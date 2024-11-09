#Importing from a script in the same directory, no need for packages (relative import)
import First #Importing whole of "First.py"
from Second import * #Importing all functions from "second.py"

First.One() #Can call any function in First through First.
Two() #Calling Two directly from Second (I think this lacks clarity of where it has come from)



#Importing from a script in a different directory (using __init__.py)
from package import * #Importing using init file in packages

Third.Three() #Imports all of "Three.py"
Four() #Four is imported in __init__.py file in package



#Importing from a script in a different subdirectory (using __init__.py in main package)
from package.subpackage import * #Importing using init file in subpackages 

Fifth.Five() #Imports all of "Five.py"
Six() #Only this function has been pulled