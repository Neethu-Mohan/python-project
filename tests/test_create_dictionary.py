import sys
sys.path.append("./projects")
from create_dictionary import check_length
from create_dictionary import create_dictionary
import pytest

keys = ["jack", "mark", "stephan", "argo", "allen", "neethu"]
values= ["34", "40", "38", "52", "63", "78"]
keys_lesslength = ["jack", "mark"]
values = ["34", "40", "38", "52", "63", "78"]
values_lesslength = ["34", "40", "38"]
key_empty = []
values_empty = []
dictionary = {'jack': '34', 'mark': '40', 'stephan': '38', 'argo': '52', 'allen': '63', 'neethu': '78'}
dictionary_keys_lesslength = {'jack': '34', 'mark': '40'}
dictionary_values_lesslength = {'jack': '34', 'mark': '40', 'stephan': '38', 'argo': None, 'allen': None, 'neethu': None}
dictionary_empty = {}
dictionary_values_empty = {'jack': None, 'mark': None, 'stephan': None, 'argo': None, 'allen': None, 'neethu': None}
list_length = 6

def test_check_length():
    assert check_length(values_empty) == 0, 'did not get the expected length when pass an empty list'
    assert check_length(values) == list_length, 'length of is wrong'

def test_create_dictionary():
    assert create_dictionary(keys, values) == dictionary, 'did not get the expected dictionary when pass keys and values of same length'
    assert create_dictionary(keys_lesslength, values) == dictionary_keys_lesslength, 'did not get the expected dictionary when pass length of keys is less than length values'
    assert create_dictionary(keys, values_lesslength) == dictionary_values_lesslength, 'did not get the expected dictionary when pass length of values is less than length keys'
    assert create_dictionary(key_empty, values_empty) == dictionary_empty, 'did not get the expected dictionary when pass length of keys and values are empty'
    assert create_dictionary(key_empty, values) == dictionary_empty, 'did not get the expected dictionary when pass empty keys and non empty values'
    assert create_dictionary(keys, values_empty) == dictionary_values_empty, 'did not get the expected dictionary when pass non empty keys and empty values'





