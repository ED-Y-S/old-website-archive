#!/usr/bin/python3

'''
This more advanced wget program is more versatile.
It uses command line arguments to specify which URL should be downloaded, and where to save it.
'''

import argparse
import requests

parser = argparse.ArgumentParser(description='Download a webpage')
parser.add_argument('--url', default = 'dracula.html',help='the url to download from the internet') # if --url does not appear when typing in the terminal, the output be defaulted by the "default"
parser.add_argument('--filename', default = 'https://www.gutenberg.org/files/345/345-h/345-h.htm',help='the path on the local computer to save the file')
args = parser.parse_args()
'''
# process command line args
parser = argparse.ArgumentParser(description='Download a webpage')
parser.add_argument('url', help='the url to download from the internet')
parser.add_argument('filename', help='the path on the local computer to save the file')
args = parser.parse_args()
'''
'''
# download the url
r = requests.get(args.url)
text = r.text

# save the file
with open(args.filename, 'w', encoding='utf-8') as f:
    f.write(text)
'''