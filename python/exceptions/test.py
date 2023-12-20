#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    for i in range(x):
        try:  
            mike=int(my_list[i])    
            print(mike,end="")
                        
        except IndexError:
            continue
        except ValueError:
            continue
    print()    
    return (mike)           
    

#my_list = [1, 2, "mike", 4, 5]
#safe_print_list_integers(my_list,3)







#my_list can contain any type (integer, string, etc.)
#All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
#x represents the number of elements to access in my_list
#x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur    