from zipfile import ZipFile
import zipfile
import os
import zlib


with open('Ashley-Madison.txt', 'r') as t:
    lines = t.read()
    lines = lines.encode('ascii')
    lines = lines.split()
    


for line in lines:
    try:
        with ZipFile('whitehouse_secrets.zip') as zf:
            password = line
            zf.extractall(pwd=password)
            print('password=', password)
            break
    except RuntimeError:
        pass
    except zlib.error:
        pass
    except zipfile.BadZipFile:
        pass
