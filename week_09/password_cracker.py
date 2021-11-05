from zipfile import ZipFile
import os

path = 'D:\CSCI40\eddie-shi.github.io\week_09'
os.chdir(path)

with open('Ashley-Madison.txt', 'rb') as t:
    lines = t.readlines()


for line in lines:
    try:
        with ZipFile('whitehouse_secrets.zip') as zf:
            password = line
            zf.extractall(pwd=password)
        print('password=', password)
    except RuntimeError:
        pass