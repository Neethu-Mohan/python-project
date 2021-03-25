"""
This program receives a file and returns ten IP addresses from which there were most requests

"""

import os
from operator import itemgetter

def get_file(file_path):
    if validate_file(file_path):
        return True
    else:
        return False


def validate_file(filepath):
    if os.path.isfile(filepath):
        return True
    else:
        print ("File does not exist")
        return False

def retrieve_file_content(filepath):
    if validate_file(filepath):
        fileRef =  open(filepath, 'r')
        return fileRef.read()
    else:
        return ""

def get_ipaddress(filecontent):
    lines = filecontent.split("\n")
    ipaddress = []
    for line in lines:
        words = line.split(" ")
        ipaddress.append(words[0])
    return(ipaddress)

def check_occurance(ipaddress_value):
    ipaddress_dictionary = {}
    for word in ipaddress_value:
        count = ipaddress_dictionary.get(word, 0)
        count = count + 1
        ipaddress_dictionary[word] = count
    return(ipaddress_dictionary)

def get_highest_requested_ipaddress(ipaddress_dictionary):
    most_requested_ips = []
    highest_requested = sorted(ipaddress_dictionary.items(), key=itemgetter(1))
    most_requested = highest_requested[-10:] 
    for item in most_requested:
        most_requested_ips.append(item[0])
    return (most_requested_ips)

def create_dictionary(ipaddr, count=1):   
    ipaddress_dictionary = {}
    ipaddress_dictionary [ipaddr] = count
    return ipaddress_dictionary



