#!/usr/bin/python3
MyList = __import__('my_list').MyList
import random
my_list = MyList()
for i in range(1,6):
    my_list.append(random.randint(0,10))
#my_list.append(1)
#my_list.append(4)
#my_list.append(2)
#my_list.append(3)
#my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
