
import sqlite3
import argparse
from flask import Flask,abort,send_file, make_response, request
from pathlib import Path
from flask.templating import render_template
from datetime import datetime  
import markdown_compiler as mc
import bleach

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
    WHERE username=? --- Question mark means that we dont know what it is, but will come later
      AND password=?;
    """
    print('is_valid_login: sql=',sql)
    cur = con.cursor()
    cur.execute(sql, [username,password]) #the bracket is parameter
    rows = cur.fetchall()
    # if the total number of rows returned is 0,
    # then no username/password combo was not found
    if len(list(rows))==0:
        return False

    # if the total number of rows returned is > 0,
    # then the username/password combo was found
    else:
        return True
def can_register(con, username):
    sql = """
    SELECT username
    FROM users
    WHERE username=?; --- Question mark means that we dont know what it is, but will come later
    """
    print('is_valid_login: sql=',sql)
    cur = con.cursor()
    cur.execute(sql, [username]) #the bracket is parameter
    rows = cur.fetchall()
    if len(list(rows))==0:
        return True

    # if the total number of rows returned is > 0,
    # then the username/password combo was found
    else:
        return False
def url_to_html(comment):
    if comment is not None:
        comment_list=comment.split(' ')
        if any('https://' in word for word in comment_list) or any('http://' in word for word in comment_list):
            print(comment_list)
            comment_link = bleach.linkify(comment)
            comment_converted=mc.compile_lines('\n'+comment_link+'\n')
            comment_converted_clean=bleach.clean(comment_converted, tags=['a', 'abbr', 'acronym', 'b', 'blockquote', 
            'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'p'], attributes=['style', 'href', 'rel'], styles=['color'])
            return comment_converted_clean
        else:
            comment_converted=mc.compile_lines('\n'+comment+'\n')
            comment_converted_clean=bleach.clean(comment_converted, tags=['a', 'abbr', 'acronym', 'b', 'blockquote', 
            'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'p'], attributes=['style', 'href'], styles=['color'])
            return comment_converted_clean
    else:
        return comment

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
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    is_logged_in = is_valid_login(con, username, password)
    return render_template('root.html', messages = messages, is_logged_in=is_logged_in)

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
            response = make_response(render_template('login.html', is_logged_in= True))
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

@app.route('/create_message',methods=['GET','POST'])
def post():
    con = sqlite3.connect(args.db_file)
    cur = con.cursor()
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    id_user = ''
    if username is not None:
        cur.execute("SELECT * FROM users where username=?",[str(username)])
        for row in cur.fetchall():
            id_user+=str(row[0])
    else:
        pass
    time = datetime.now()
    time = time.strftime("%Y-%m-%d %H:%M:%S")
    message = url_to_html(request.form.get('message')) 
    is_logged_in = is_valid_login(con, username, password)
    has_clicked_form = message is not None
    if is_logged_in:
        if has_clicked_form:
            cur.execute("INSERT INTO messages (sender_id,message,created_at) values (?,?,?)", [str(id_user),str(message),str(time)])
            con.commit()
            return render_template('create_message.html', posted = True, is_logged_in = True)
        else:
            render_template('create_message.html', posted = False, is_logged_in = True)
        return render_template('create_message.html', is_logged_in = True)
    else:
        return render_template('create_message.html', not_logged_in = True)  
    

 

@app.route('/create_user',methods=['GET','POST'])
def register():
    con = sqlite3.connect(args.db_file)
    cur = con.cursor()
    print_debug_info()
    create_username = request.form.get('username')
    create_password = request.form.get('password')
    password_again = request.form.get('password_again')
    create_age = request.form.get('age')
    has_clicked_form = create_username is not None
    if has_clicked_form:
        register_true = can_register(con, create_username)
        if register_true and create_password !=None and create_password !='' and password_again == create_password :
            cur.execute("INSERT INTO users (username, password, age) values (?,?,?)", [str(create_username),str(create_password),str(create_age)])
            con.commit()
            return render_template('create_user.html', is_created = True)
        elif register_true and create_password !=None and create_password !='' and password_again != create_password:
            return render_template('create_user.html', password_check_error = True) 
        if register_true is False: 
            return render_template('create_user.html', display_error = True)
        if create_password == None or create_password == '':
            return render_template('create_user.html', no_password = True)  
    else:
        render_template('create_user.html')  
    return render_template('create_user.html')
@app.route('/base')
def menu():
    print_debug_info()
    return render_template('base.html')


app.run(host="0.0.0.0", port=80)