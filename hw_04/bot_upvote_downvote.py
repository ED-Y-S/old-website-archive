from re import sub
from nltk.featstruct import subsumes
import praw
import random
import datetime
import time
import prawcore
from textblob import TextBlob
reddit = praw.Reddit('bot')
vote_submission = 0
vote_comment = 0
for submission in list(reddit.subreddit("BotTown2").new(limit=500)):
    print("one submission is being processed")
    submission.comments.replace_more(limit=None, threshold=0)
    blob = TextBlob(str(submission.title))
    pop = blob.sentiment.polarity
    not_my_comments = []
    if 'Elon' in submission.title or 'Elon Musk' in submission.title or 'Musk' in submission.title:
        if str(submission.author) == 'ElonMuskBadTakeBot':
            print("my submission")
            pass
        else:
            print("one submission with elon musk and not mine is being processed")
            if pop > 0:
                submission.downvote()
                vote_submission+=1
                print("Downvoting submission", vote_submission)
            if pop <= 0:
                submission.upvote()
                vote_submission+=1
                print("Upvoting comment", vote_submission)
            else:
                pass
    for comment in submission.comments:
        if str(comment.author) != 'ElonMuskBadTakeBot':
            not_my_comments.append(comment)
    for comment in not_my_comments:
        blob = TextBlob(str(comment.body))
        pop = blob.sentiment.polarity
        try:
            if 'Elon' in comment.body or 'Elon Musk' in comment.body or 'Musk' in comment.body:
                if pop > 0:
                    comment.downvote()
                    vote_comment+=1
                    print("Downvoting comment", vote_comment)
                if pop <= 0:
                    comment.upvote()
                    vote_comment+=1
                    print("Upvoting comment", vote_comment)   
            else:
                pass
        except prawcore.exceptions.NotFound:
            print("comment deleted")
            pass

    print("one submission checked")