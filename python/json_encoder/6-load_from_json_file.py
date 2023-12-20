#!/usr/bin/env python3

import json
#filename="my_dict.json"
def load_from_json_file(filename):
  with open(filename, 'r', encoding='utf-8') as json_file:
    try:
        if json_file:
            loaded_data = json.load(json_file)
            return (loaded_data)
        else:
           raise FileNotFoundError
    except ValueError:
        return ("[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)")
    except FileNotFoundError:
        return (f"[FileNotFoundError] [Errno 2] No such file or directory: '{filename}'") 
#load_from_json_file(filename)            