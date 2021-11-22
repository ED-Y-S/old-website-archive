from re import sub
from nltk.featstruct import subsumes
import praw
import random
import datetime
import time
reddit = praw.Reddit('bot')
for i in range(5):
    try:
        top = list(reddit.subreddit('elonmusk').hot(limit = None))
        submission = random.choice(top)
        title = submission.title
        url = submission.url
        text = submission.selftext
        if url:
            reddit.subreddit('BotTown').submit(title, url= url)
        else:
            reddit.subreddit('BotTown').submit(title, selftext= text)
    except praw.exceptions.InvalidURL:
        print('The URL is not Valid')
        pass
        

    


