#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictioanry.keys():
        del a_dictioanry[key]
        return a_dictionary
