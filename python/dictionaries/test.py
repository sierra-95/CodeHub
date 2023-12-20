#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key in a_dictionary.keys():
            a_dictionary[key] =value
            return a_dictionary
        
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new=update_dictionary(a_dictionary, 'language', "Python")  
print(new) 

   