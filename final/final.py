import sqlite3
import argparse
from flask import Flask,abort,send_file, make_response, request
from pathlib import Path
from flask.templating import render_template

########################################
# flask/db setup
########################################

from flask import Flask, render_template, request
app = Flask(__name__)

# sqlite3 is built in python3, no need to pip3 install
import sqlite3

# process command line arguments
import argparse
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()

########################################
# helper functions
########################################

def print_debug_info():
    '''
    Print information stored in GET/POST/Cookie variables to the terminal.
    '''
    # rewuest is different from request*S*
    # these variables are set by the information after the ? in the url;
    # in the information after the ? is called the query arguments
    # these variables are just for one webpage
    print("request.args.get('username')=",request.args.get('username'))
    print("request.args.get('password')=",request.args.get('password'))
    # this information comes from a POST form
    # the methods for the route must inclue POST
    print("request.form.get('username')=",request.form.get('username'))
    print("request.form.get('password')=",request.form.get('password'))
    # these variablespass between pages
    # these are "persistent"; the others are not
    print("request.cookies.get('username')=",request.cookies.get('username'))
    print("request.cookies.get('password')=",request.cookies.get('password'))


def is_valid_login(con, username, password):
    '''
    Return True if the given username/password is a valid login;
    otherwise return False.
    '''

    # query the database for users with the given username/password
    sql = """
    SELECT username,password
    FROM users
    WHERE username='"""+str(username)+"""'
      AND password='"""+str(password)+"""';
    """
    print('is_valid_login: sql=',sql)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    # if the total number of rows returned is 0,
    # then no username/password combo was not found
    if len(list(rows))==0:
        return False

    # if the total number of rows returned is > 0,
    # then the username/password combo was found
    else:
        return True


########################################
# custom routes
########################################

app = Flask(__name__)
@app.route('/static/<path:name>', methods=['GET'])
def get_output_file(name):
    print_debug_info()
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
    print_debug_info()
    messages = []
    
    con = sqlite3.connect(args.db_file)
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
    return render_template('root.html', messages = messages)

@app.route('/login',methods=['GET','POST'])
def login():
    con = sqlite3.connect(args.db_file)
    print_debug_info()
    form_username = request.form.get('username')
    form_password = request.form.get('password')
    print("form_username", form_username)
    print('form_password', form_password)

    has_clicked_form = form_username is not None
    print('has_clicked_form', has_clicked_form)
    
    if has_clicked_form:
        login_info_correct = is_valid_login(con, form_username, form_password)
        
        if login_info_correct:
            #if someone has clicked on the form;
            #and the information is correct
            #then we should set cookies
            response = make_response(render_template('login.html'))
            response.set_cookie('username', form_username)
            response.set_cookie('password', form_password)
            return response
        else:
            return render_template('login.html', display_error = True)
    else:
        # if someone clicked on the form;
        # and the form information is wrong;
        # then we should display an error
        render_template('login.html')
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    print_debug_info()
    response = make_response(render_template('logout.html'))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('password', '', expires=0)
    return response

@app.route('/create_message')
def post():
    print_debug_info()
    return render_template('create_message.html')
@app.route('/create_user')
def register():
    print_debug_info()
    return render_template('create_user.html')
@app.route('/base')
def menu():
    print_debug_info()
    return render_template('base.html')


app.run()