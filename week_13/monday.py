from flask import Flask
from flask.templating import render_template
app = Flask(__name__)
@app.route('/')
def root():
    return "Hello B Words!"
@app.route('/login')
@app.route('/logout')
@app.route('/create_message')
@app.route('/create_user')


app.run()


'''
@app.route('/users') #add a path
def users():
    username = "Mike"
    users = ['mike', 'kristen', 'issac']
    return render_template('users.html', username=username, users=users)
'''