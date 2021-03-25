"""
This program checks whether the input string matches the following rules.
    * the password must begin with a latin letter,
    * the password can consist of Latin letters, numbers, dot and minuses,
    * the password must end only with a latin letter or number;
    * minimum password length is one character
    * maximum password length is 20 characters
    
"""

import getpass
password_length_max = 20
password_length_min = 1

def check_password_length(word):
    if len(word) > password_length_max:
        return False
    elif len(word) < password_length_min:
        return False
    else:
        return True

def check_alphabetic(letter):
        if letter.isalpha():
            return True
        else:
            return False

def check_alphanumeric(letter):
        if letter.isalnum():
            return True
        else:
            return False

def check_index(word, letter):
    index = word.index(letter)
    return index

def first_character_rule(word):
    if check_alphabetic(word[0]):
        return True
    else:
        return False

def last_character_rule(word):
    if check_alphanumeric(word[len(word) - 1]):
        return True
    else:
        return False

def all_character_rule(word):
    for character in word:
        if not (check_alphanumeric(character) or character == "." or character == "-"):
            return False
    return True

def character_validation(word):
    if not check_password_length(word):
        print("invalid password length")
        return False
    elif not first_character_rule(word):
        print("invalid first character")
        return False
    elif not last_character_rule(word):
        print("invalid last character")
        return False
    elif not all_character_rule(word):
         print("the password can only consist of Latin letters, numbers, dot and minuses")
         return False
    else:
        return True



