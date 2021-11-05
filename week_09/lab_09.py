import os

path = 'D:\CSCI40\eddie-shi.github.io\week_09'
os.chdir(path)

from zipfile import ZipFile
with ZipFile('guido_secrets.zip') as zf:
    password = b'BFDL'
    zf.extractall(pwd=password)