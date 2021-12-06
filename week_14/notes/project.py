########################################
# flask/db setup
########################################

from flask import Flask, render_template, request, make_response
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

@app.route('/')     
def root():
    con = sqlite3.connect(args.db_file)
    print_debug_info()

    username = print("request.cookies.get('username')=",request.cookies.get('username'))
    password = print("request.cookies.get('password')=",request.cookies.get('password'))
    is_logged_in = is_valid_login(con, username, password)

    return render_template('root.html', is_logged_in=is_logged_in)


@app.route('/login', methods=['GET','POST']) #GET by default
def login():
    con = sqlite3.connect(args.db_file)
    print_debug_info()
    form_username = request.form.get('username')
    form_password = request.form.get('password')
    print("form_username", form_username)
    print('form_password', form_password)

    has_clicked_form = form_username is not None
    print('has_clicked_form', has_clicked_form)

    

    

    # if no one clicked on the forml
    # do nothing
    
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
    

@app.route('/logout')     
def logout():
    print_debug_info()
    response = make_response(render_template('logout.html'))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('password', '', expires=0)
    return response
    

@app.route('/create_message')     
def create_message():
    print_debug_info()
    return render_template('create_message.html')
    

@app.route('/create_user')     
def create_user():
    print_debug_info()
    return render_template('create_user.html')
    

########################################
# boilerplate
########################################

if __name__=='__main__':
    app.run()
