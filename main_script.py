from Application import First_script, Two_Func
from Application.package import *
from Application.package.subpackage import *


def main():

    print(First_script.One_Func())
    print(Two_Func())
    

    print(Third_script.Three_Func())
    print(Four_Func())


    print(Fifth_script.Five_Func())
    print(Six_Func())
        
if __name__ == "__main__":
    main()