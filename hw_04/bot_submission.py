from re import sub
from nltk.featstruct import subsumes
import praw
import random
import datetime
import time
reddit = praw.Reddit('bot')

while True:
    try:
        top = list(reddit.subreddit('elonmusk').hot(limit = None))
        submission = random.choice(top)
        title = submission.title
        url = submission.url
        text = submission.selftext
        if url:
            reddit.subreddit('BotTown2').submit(title, url= url)
            print("url/media submission")
        else:
            reddit.subreddit('BotTown2').submit(title, selftext= text)
            print("text submission")
    except praw.exceptions.InvalidURL:
        print('The URL is not Valid')
        pass
    time.sleep(1)
    
    

    


