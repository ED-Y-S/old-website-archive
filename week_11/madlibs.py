import random
import praw
import time

from praw.reddit import Submission
'''
This lab has three tasks.
TASK 1:
Implement the `generate_comment` function below.
TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].
TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).
SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.
'''

madlibs = [
    "[PYTHON] is a [GREAT] [TOOL].  It [CAN_DO] [LOTS] of [STUFF]. [EVERYONE] [SHOULD] [LEARN] [PYTHON] and [BECOME] a [PROGRAMMER].",
    "I [LOVE] [PYTHON].",
    ]

replacements = {
    'PYTHON' : ['Python', 'Programming', 'Coding'],
    'GREAT' : ['great', 'magnificent', 'fantastic', 'wonderful'],
    'TOOL' : ['tool', 'skill'],
    'CAN_DO' : ['can do', 'is able to do', 'accomplishes', 'enables me to do', 'helps me do'],
    'LOTS'  : ['lots', 'a whole lot', 'ridiculous amounts'],
    'STUFF' : ['stuff', 'things', 'fun things'],
    'LOVE' : ['love', 'adore', 'like'],
    'EVERYONE' : ['Everyone', 'Everyone (even humanities majors)', 'Everyone, yes that means you,', 'All students', 'People everywhere', 'You'],
    'SHOULD' : ['should', 'must', 'need to'],
    'BECOME' : ['become', 'turn into', 'try to be'],
    'PROGRAMMER' : ['programmer', 'developer', 'pythonista', 'software engineer'],
    'LEARN' : ['learn', 'master', 'study'],
    }


def generate_comment():

    m = random.choice(madlibs)
    for k in replacements.keys():
        m = m.replace('['+k+']', random.choice(replacements[k]))

    return m
reddit = praw.Reddit('bot')
url = 'https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/'
submission = reddit.submission(url=url)
for i in range(69): # spam it for 69 times
    submission.comments[0].reply(generate_comment())
    submission.reply(generate_comment())
    print('made a comment, i = ',i)
    time.sleep(600) #let the bot "sleep" for 10 minutes
    

    
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''