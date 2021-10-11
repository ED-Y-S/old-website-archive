#print('hello world')

#/users/eddie/documents/github/eddie-shi.github.io/week_05 is an "absolute path"; 
# absolute path is a path that works everywhere
# a relative path is just a reference to a file, but an absolute path
# working directory is where you are located
# pwd = print working diretory
# put the working directory at the beginning of the relative path to make an absolut path
# cd = change directory
# cd .. = move back/up one directory

#with open('blurb') as c: 
#xxx/blurb can get you the 'blurb' file intead thats in the 'xxx' directory
'''with open('blurb', encoding ='utf8') as c:  these are same for MacOS but not for Windows
#change encoding at the bottom right of VSC; the encoding = 'xxx', xxx must match the encoding with the file looking for
text = c.read() # the read file doesn't have to blurb
print(text)
'''

#import os
#print(os.getcwd()) #return the string of the working directory

'''
with open ('blurb', 'w' , encoding = 'utf-8') as c:
    text = c.write()
print (text)
'''
with open('week_06/blurb', 'tr') as c: #mode contains 'b' = get bytes; mode with 't' = get a string; 'r'=read ('tw' for write)
    text = c.read()
with open('week_06/blurb', 'br') as c:
    byte = c.read()