#!/usr/bin/python3
'''
Create a database for the Twitter project.
'''

# sqlite3 is built in python3, no need to pip3 install
import sqlite3

# process command line arguments
import argparse
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()

# connect to the database
con = sqlite3.connect(args.db_file) # con = connection; one of the variables for the whole file
cur = con.cursor() # cursor() allows to run multiple commands simultaneously; in the class, one cur() for whole file

# create the users table
sql = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);
'''
cur.execute(sql) # pass the sql to SQL database; this is what connects python to SQL
con.commit() # saves the changes

# insert some dummy (example) data
cur.execute('''insert into users (username, password, age) values ('Trump', 'I AM TRUMP', 76);''')
cur.execute('''insert into users (username, password, age) values ('Biden', '54321', 79);''')
cur.execute('''insert into users (username, password, age) values ('Evan', 'correct horse battery staple', 3);''')
cur.execute('''insert into users (username, password, age) values ('Isaac', 'guaguagua', 3);''')
cur.execute('''insert into users (username, password, age) values ('Mike', '524euTjrWm6uK2C5iw8mC6aNgX1JI78o', 35);''')
cur.execute('''insert into users (username, password) values ('Kristen', 'Possible-Rich-Absolute-Battle');''')
con.commit()

# create the messages table
sql = '''
create table messages (
    id integer primary key,
    sender_id integer not null,
    message text not null,
    created_at timestamp not null default current_timestamp
    );
'''
cur.execute(sql)
con.commit()

# insert some dummy data
sql = '''
insert into messages (sender_id,message,created_at) values
    (1, 'I''m a baby', '2021-11-17 14:30:00'),
    (2, 'I''m a baby', '2021-11-17 14:30:00'),
    (3, 'I''m a baby', '2021-11-17 14:33:01'),
    (4, 'I''m a baby', '2021-11-17 14:35:45');
'''
cur.execute(sql)
con.commit()

sql='''
insert into messages (sender_id,message,created_at) values
    (3, 'I''m actually a toddler','2021-11-17 14:37:45');
'''
cur.execute(sql)
con.commit()

sql='''
insert into messages (sender_id,message,created_at) values
    (5, 'I''m an adult', '2021-11-17 14:30:00'),
    (5, 'SQL is the best!!', '2021-11-18 14:30:00'),
    (6, 'I''m an adult', '2021-11-17 14:33:01'),
    (6, 'WTF is SQL?!  I thought you liked the snake thing.', '2021-11-17 14:35:45');
'''
cur.execute(sql)
con.commit()