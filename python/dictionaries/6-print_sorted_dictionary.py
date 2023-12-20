#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))


#Here, we use the sorted function to sort the keys of the dictionary (a_dictionary.keys()) in alphabetical order.
# The sorted keys are stored in the sorted_keys list.
#This loop iterates through each sorted key in sorted_keys. For each key, it retrieves the corresponding value from the dictionary using a_dictionary[key], 
#and then it uses the print function to display the key and value in the format "key: value".