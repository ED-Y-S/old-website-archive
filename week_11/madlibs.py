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
    "I put [ART] in the [FART]", "I keep forgetting that [YOU] are still alive.", "Due to inflation [420] has gone up by [69]", "[NAUGHTIUS] [MAXIMUS]"]

replacements = {
    'ART' : ['art', 'boot', 'laughter'],
    'FART' : ['fart', 'booty', 'slaughter'],
    'YOU': ['Bernie', 'my sexual life', 'my humor'],
    '420': ['420', '71', '69'],
    '69': ['69','71','69'],
    'NAUGHTIUS': ['Naughtius', 'Biggus', 'Deezus'],
    'MAXIMUS': ['Maximus', 'Dickus', 'Nuttus']
    }


def generate_comment():

    m = random.choice(madlibs)
    for k in replacements.keys():
        m = m.replace('['+k+']', random.choice(replacements[k]))
    return m
    
reddit = praw.Reddit('bot')
url = 'https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/'
submission = reddit.submission(url=url)
for i in range(100): # spam it for 100 times
    submission.comments[i].reply(generate_comment())
    submission.reply(generate_comment())
    print('made a comment, i = ',i)
    time.sleep(60*5) #let the bot "sleep" for 5 minutes
    

    
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