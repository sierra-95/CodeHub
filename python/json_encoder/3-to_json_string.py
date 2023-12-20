#!/usr/bin/env python3
import json
def to_json_string(my_obj):
    #.dumps is for strings and dump is for file
    content=json.dumps(my_obj)
    return content