import sys
sys.path.append("./projects")
from password_validation import character_validation
import pytest

vaild_password = 'abc.123.ABC.00--3'
invalid_length_password1 = "abc.123.ABC.00--312345"
invalid_length_password2 = ""
invalid_start_character1 = "1abc.123.ABC.00--3"
invalid_start_character2 = "$abc.123.ABC.00--3"
invalid_last_character = "abc.123.ABC.00--?"

def test_character_validation():
    assert character_validation(vaild_password) == True, 'did not get expected boolean evenif password is valid'
    assert character_validation(invalid_length_password1) == False, 'did not get expected boolean when password is invalid'
    assert character_validation(invalid_length_password2) == False, 'did not get expected boolean when password is invalid'
    assert character_validation(invalid_start_character1) == False, 'did not get expected boolean when password is invalid'
    assert character_validation(invalid_start_character2) == False, 'did not get expected boolean when password is invalid'
    assert character_validation(invalid_last_character) == False, 'did not get expected boolean when password is invalid'
 
