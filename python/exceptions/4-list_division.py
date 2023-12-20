#!/usr/bin/python3
#almost works but i gave up
def list_division(my_list_1, my_list_2, list_length):
    newlist=[]
    try:
        if len(my_list_1)==len(my_list_2):
            for i in range(len(my_list_1)):
                if int(my_list_1[i]):
                    newlist.append(int(my_list_1[i])/int(my_list_2[i]))
                else:
                     raise ValueError                                
            return newlist
        else:
              raise IndexError       
    except ZeroDivisionError:
            print("Division by zero denied")
    except ValueError:
             print()
             print("wrong type")
    except IndexError:
           print("out of range")              



#my_list_1 = [10, 8, 4]
#y_list_2 = [2, 4, 4]  
#list_division(my_list_1,my_list_2,2)     