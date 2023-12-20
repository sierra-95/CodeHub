#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
        print("{}".format(value),end="")
        print()
        return True
    except ValueError:
        return False
    
    




#Returns True if value has been correctly printed (it means the value is an integer)
#Otherwise, returns False
