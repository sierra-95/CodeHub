#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            mike=my_list[i]
            print(mike,end="")
        print()
        return mike    

    except IndexError:
        print()
        return mike  
           



#my_list = [1, 2, 3, 4, 5]
#safe_print_list(my_list,len(my_list)+2)
#x represents the number of elements to print
#x can be bigger than the length of my_list