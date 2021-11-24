from re import sub
from nltk.featstruct import subsumes
import praw
import random
import datetime
import time
reddit = praw.Reddit('bot')

for i in range(200):
    try:
        top = list(reddit.subreddit('elonmusk').hot(limit = None))
        submission = random.choice(top)
        title = submission.title
        url = submission.url
        text = submission.selftext
        if url:
            reddit.subreddit('BotTown1').submit(title, url= url)
        else:
            reddit.subreddit('BotTown1').submit(title, selftext= text)
    except praw.exceptions.InvalidURL:
        print('The URL is not Valid')
        pass
    print("submission ", i)
    

    


