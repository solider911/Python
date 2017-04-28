#!/usr/bin/python
#Filename:using_name.py

import mymodule

mymodule.sayhi()

print("Version："+mymodule.version)

if  __name__ == "__main__":
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

    
dir(mymodule)
