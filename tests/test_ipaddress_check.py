import sys
sys.path.append("./projects")
from ipaddress_check import check_occurance
from ipaddress_check import get_highest_requested_ipaddress
from ipaddress_check import get_file
from ipaddress_check import retrieve_file_content
from ipaddress_check import get_ipaddress
import pytest
file_content = "66.249.73.135 this is a test file"
retrived_ip = ['66.249.73.135']
ip_values = ('66.249.73.135', '108.28.155.98', '108.28.155.98', 
             '108.28.155.98', '108.28.155.98', '108.28.155.98', '108.28.155.98',
              '54.241.62.89', '120.136.4.243', '66.249.73.185', '195.194.187.106', 
              '66.249.73.185', '66.249.73.185', '176.31.39.30', '176.31.39.30', 
              '116.199.211.249', '46.105.14.53', '5.10.83.53', '66.249.73.135', 
              '92.115.179.247', '92.115.179.247', '92.115.179.247', '92.115.179.247',
              '92.115.179.247', '92.115.179.247', '5.10.83.53', '46.119.114.245', 
              '173.231.106.34', '66.169.220.99', '66.249.73.135', '50.16.19.13', 
              '5.10.83.21', '208.91.156.11', '66.249.73.135', '66.249.73.135', 
              '46.105.14.53', '68.180.224.225', '91.151.182.109', '91.151.182.109')
ip_values_empty = ""
request_counts_empty = {}
request_counts = {'66.249.73.135': 5, '108.28.155.98': 6, '54.241.62.89': 1, 
                  '120.136.4.243': 1, '66.249.73.185': 3, '195.194.187.106': 1, '176.31.39.30': 2, 
                  '116.199.211.249': 1, '46.105.14.53': 2, '5.10.83.53': 2, '92.115.179.247': 6, 
                  '46.119.114.245': 1, '173.231.106.34': 1, '66.169.220.99': 1, '50.16.19.13': 1, 
                  '5.10.83.21': 1, '208.91.156.11': 1, '68.180.224.225': 1, '91.151.182.109': 2}
most_occured = ['208.91.156.11', '68.180.224.225', '176.31.39.30', '46.105.14.53', '5.10.83.53',
                 '91.151.182.109', '66.249.73.185', '66.249.73.135', '108.28.155.98', '92.115.179.247']
most_occured_empty = []

def test_get_file():
    assert get_file('projects/file_test.log') == True, 'not getting a file which exists'
    assert get_file('fileunknow') == False, 'getting a file which is not exists'

def test_retrieve_file_content():
    retrieve_file_content('projects/file_test.log') == file_content, 'can not read the file'
    retrieve_file_content('fileunknown') == False, 'shows contents of a non existing file'

def test_get_ipaddress():
    assert get_ipaddress(file_content) == retrived_ip, 'did not retrive ip address from the file contents'

def test_check_occurance():
    assert check_occurance(ip_values) == request_counts, 'did not get the count of occurance of the passed ipaddress'
    assert check_occurance(ip_values_empty) == request_counts_empty, 'did not get the count of occurance when empty list of ipaddress passes '

def test_get_highest_requested_ipaddress():
    assert get_highest_requested_ipaddress(request_counts)== most_occured, 'did not get most occured ipaddress'
    assert get_highest_requested_ipaddress(request_counts_empty)== most_occured_empty, 'did not get most occured ipaddress when passess empty dictionary of ipaddress and its counts'






