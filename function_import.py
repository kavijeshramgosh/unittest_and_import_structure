'''

Here are some examples on how you can import scripts or functions from Application/ to another
file in the same directory as Application/ by setting up Application/ using __init__.py

'''

# Uses the __init__.py within Application/ to import whatever is in __all__
from Application import First_script,Two_Func 


print(First_script.One_Func()) # Every function within First_script has been imported as per __init__.py
print(Two_Func()) # Only Two_Func is imported as listed within __init__.py


# Uses the __init__.py within packages/ to import whatever is in __all__
from Application.package import * 

print(Third_script.Three_Func()) # Every function within Third_script is callable

print(Four_Func()) # Only Four_Func has been imported


# Uses the __init__.py within subpackages/ to import whatever is in __all__
from Application.package.subpackage import * 

print(Fifth_script.Five_Func()) # Every function within Fifth_script is callable

print(Six_Func()) # Only Six_Func has been imported