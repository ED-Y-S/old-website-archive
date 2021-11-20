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
    'Who is running this lame [COLLECTION] of [BOTS] & [TROLLS] anyway? Try harder! I’m an [ENGINEER], knucklehead. Just do [“BUSINESS”] on the side.',
    'Tesla is filing a [LAWSUIT] against [ALAMEDA COUNTY] immediately. The unelected & ignorant [“INTERIM HEALTH OFFICER”] of [ALAMEDA] is acting contrary to the [GOVERNOR], the President, our Constitutional freedoms & just plain common sense!', 
    '(Formerly) [MAINSTREAM MEDIA] has systemic negative & political bias about almost everything. Reading major [NEWSPAPERS] makes you feel sad & [ANGRY]. That’s why they’re being [CRUSH] by [@JOEROGAN]. ',
    '[EXTREMELY] big difference between died because of or died with. Also, did the person actually have [C19] or did they just have [C19] symptoms? It’s almost impossible to [DIE] without feeling [WEAKNESS], shortness of breath or other [C19] symptoms, unless you were crushed by a falling [PIANO].',
    'Another reason reported [MORTALITY] rate is overstated is that dying [*WITH*] [COVID] is not same as dying [*FROM*] covid. [MEDIA] keeps reporting former, not latter.',
    'Well said! Please run for [OFFICE]. The politicians & unelected bureaucrats who stole our [LIBERTY] should be [TARRED], feathered & [THROWN] out of [TOWN]!']

replacements = {
    'COLLECTION' : ['group', 'herd', 'wave', 'kind', 'mass', 'collection'],
    'BOTS' : ['robot', 'losers', 'braindead', 'mentally challenged', 'bots'],
    'TROLLS': ['no-life losers', 'losers', 'no-lifers','edgelords', 'bad jokers'],
    'ENGINEER': ['Gamer', 'Memer', 'Engineer', 'Billionare', 'King'],
    '"BUSINESS"': ['your mom', 'drugs', '"business"', '69', 'gamer moment'],
    'LAWSUIT': ['action', 'trial', 'epic moment', 'gamer moment', 'lawsuit'],
    'ALAMEDA COUNTY': ['the US', 'Mars', 'the Earth', 'the poor people','Alameda County'],
    'ALAMEDA': ['the US', 'Mars', 'the Earth', 'poor people','Alameda County'],
    '“INTERIM HEALTH OFFICER”': ['clown', 'gamer', 'Interim Health Officer', 'tax-paid official', 'Joker'],
    'GOVERNOR': ['citizens', 'rich people', 'me', 'Governor','Alameda'],
    'MAINSTREAM MEDIA':['Fox News', 'CNN', 'Twitter', 'Daily Wire', 'Mainstream Media'],
    'NEWSPAPERS': ['newspapers', 'news outlet', 'news website', 'media', 'news'],
    'ANGRY': ['angry', 'outraged', 'grumpy','not epic', 'not feeling the vibe'],
    'CRUSHED': ['shit on', 'dunked on', 'crushed', 'destroyed', 'bombed'],
    '@JOEROGAN': ['your mom\'s ass','Alex Jones', 'Ben Shapiro', '@joerogan', 'me'],
    'EXTREMELY': ['Very', 'Tremendous', 'Gigantic', 'Enormous', 'Extremely'],
    'C19': ['Ligma', 'Sigma', 'COVID','COVID-19','C19'],
    'DIE': ['die', 'not-living', 'get robloxed', 'not-breathing', 'get oof-ed', 'pass away'],
    'WEAKNESS':['not epic', 'weakness', 'exhaustion', 'fatique','weakness'],
    'PIANO':['piano', 'SpaceX rocket','Tesla', 'your mom', 'ass'],
    'MORTALITY': ['death', 'not-living', 'robloxed', 'not-breathing', 'oof-ed', 'pass away'],
    'COVID': ['Ligma', 'Sigma', 'COVID','COVID-19','C19'],
    '*WITH*': ['*along*', '*besides*','*with*','*accompanied by*', '*in the company of*'],
    '*FROM*': ['*by*', '*from*', '*against*','out of','of'],
    'MEDIA': ['Fox News', 'CNN', 'Twitter', 'Daily Wire', 'Mainstream Media'],
    'OFFICE': ['President', 'Governor', 'Mayor', 'Congress', 'Senate'],
    'LIBERTY':['freedom', 'sovereinty', 'human rights', 'liberty', 'independence'],
    'TARRED': ['terrified', 'ashamed', 'tarred', 'fouled', 'scared'],
    'THROWN': ['thrown', 'kicked', 'yeeted','tossed','hurled'],
    'TOWN': ['town', 'the country', 'the state', 'the planey', 'the universe']
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
    submission.comments[0].reply(generate_comment())
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