#!/usr/bin/python3

'''
A wget program is a program that "gets" something from the "w"eb,
and saves it to the local computer.
It is the "hello world" of web programming.
'''

import requests

url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm' # getting a wrong path wont get a python error; but wrong format of url will
filename = 'dracula.html'

# download the url
r = requests.get(url)
if r.status_code == 404: # the code of the website
    print('ERROR 404')
elif r.status_code == 200: # 200 = sucess
    text = r.text
elif r.status_code == 503: # 503 = no permission to the URL
    pass

# when opening an incorrect file, python gives us an error message;
# but when openning an incorrect url, python sometiems does and stimes does not give us an error

# save the file
with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)