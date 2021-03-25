"""
  This program receives two lists of different lengths. The first contains keys, and the second contains values. 
And the program creates a dictionary from these keys and values. If the key did not have enough values, the dictionary will have the value None. If
Values that did not have enough keys will be ignored.

"""

from itertools import chain, repeat
keys = []

def get_list():
    keys = [item for item in input("Enter the first list items : ").split()]
    values = [item for item in input("Enter the second list items : ").split()]
    dictionary_ouput = create_dictionary(keys, values)
    print(dictionary_ouput)

def create_dictionary(keys, values):
    difference = compare_length(keys, values)
    if difference <= 0:
        dic_value = dict(zip(keys, values))
        return dic_value
    elif difference > 0:
        dic_value = dict(zip(keys, chain(values, repeat(None))))
        return dic_value

def compare_length(keys, values):
    difference = check_length(keys) - check_length(values)
    return difference

def check_length(item):
    return len(item)

 




 