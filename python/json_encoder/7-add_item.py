#!/usr/bin/env python3
save=__import__("5-save_to_json_file").save_to_json_file
load=__import__("6-load_from_json_file").load_from_json_file
from sys import argv as av
list=[]
print(len(av))
if len(av) == 1:
    save(list,"add_item.json") 
else:
    for i in range(1,len(av)):
        list.append(av[i])
print(list)    
save(list,"add_item.json")