#!/usr/bin/python3
'''
Output a summary of the contents of the twitter database.
'''

# sqlite3 is built in python3, no need to pip3 install
import sqlite3

# process command line arguments
import argparse
from flask import Flask,abort,send_file
from pathlib import Path
from flask.templating import render_template
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()

# connect to the database
con = sqlite3.connect(args.db_file, check_same_thread=False)
cur = con.cursor()

# # print users
# print('================================================================================')
# print('users')
# print('================================================================================')
# sql = """
# select * from users;
# """
# cur.execute(sql)
# for row in cur.fetchall(): # .fetchall() gives access to all the results, NOT all rows. It's for the command above to do.
#     print('id=', row[0])
#     print('username=', row[1])
#     print('password=', row[2])
#     print('age=', row[3])
#     print('================')

# # print messages
# print('================================================================================')
# print('messages')
# print('================================================================================')
# sql = """
# select * from messages;
# """
# cur.execute(sql)
# for row in cur.fetchall():
#     print('id=', row[0])
#     print('id_sender=', row[1])
#     print('message=', row[2])
#     print('created_at=', row[3])
#     print('================')

app = Flask(__name__)
@app.route('/static/<path:name>', methods=['GET'])
def get_output_file(name):
    print(name)
    if ".." in name:
        abort(404)
    file_path = Path("D:\CSCI40\eddie-shi.github.io\week_13\static\{}".format(name))
    if file_path.is_file():
        return send_file(file_path)
    abort(404)
    return 0
@app.route('/')
def root():
    messages = []
    cur.execute('''SELECT message FROM messages ORDER BY created_at DESC''')
    for row in cur.fetchall():
        messages.append(row[0]) 
    return render_template('index.html', messages = messages)

# @app.route('/login')
# @app.route('/logout')
# @app.route('/create_message')
# @app.route('/create_user')


app.run()