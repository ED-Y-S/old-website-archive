import sqlite3
import argparse
from flask import Flask,abort,send_file
from pathlib import Path
from flask.templating import render_template

parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()

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
    
    con = sqlite3.connect(args.db_file, check_same_thread=False)
    cur = con.cursor()
    cur.execute('''SELECT * FROM messages ORDER BY created_at DESC''')
    for row in cur.fetchall():
        cur.execute('''SELECT * FROM users where id =''' + str(row[1]))
        for row2 in cur.fetchall():
            message_dic = {
            'Username' : row2[1],
            'Message' : row[2],
            'Time' : row[3],
            'Age' : row2[3]
            }
            messages.append(message_dic)
    return render_template('index.html', messages = messages)

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    return render_template('logout.html')
@app.route('/create_message')
def post():
    return render_template('create_message.html')
@app.route('/create_user')
def register():
    return render_template('create_user.html')
@app.route('/base')
def menu():
    return render_template('base.html')


app.run()