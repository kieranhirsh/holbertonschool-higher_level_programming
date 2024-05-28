#!/usr/bin/python3
''' module documentation '''
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if os.path.exists("add_item.json"):
    my_obj = load_from_json_file("add_item.json")
else:
    my_obj = []

for ii in range(1, len(sys.argv)):
    my_obj.append(sys.argv[ii])

save_to_json_file(my_obj, "add_item.json")
