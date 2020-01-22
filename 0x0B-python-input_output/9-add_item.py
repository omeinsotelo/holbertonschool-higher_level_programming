#!/usr/bin/python3
""" Adds all arguments to a list, save them to a file """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

list1 = sys.argv[1:]

try:
    list2 = load_from_json_file("add_item.json")
except:
    list2 = []

list2.extend(list1)
save_to_json_file(list2, "add_item.json")
