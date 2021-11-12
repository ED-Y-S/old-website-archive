import praw
import pprint
import os



# FIXME:
# login to reddit with your bot's credentials;
# recall that this requires creating a praw.ini file
# 
# WARNING:
# If you include any credential information in your final submission,
# you will receive NEGATIVE POINTS on your lab!!!
reddit = praw.Reddit('bot')

# connect to the "Main Discussion Thread" reddit submission
submission = reddit.submission(url='https://old.reddit.com/r/BotTown/comments/qqmr8l/main_discussion_thread/')

# FIXME:
# Click the "view more comments" buttons in the reddit submission in order to download all comments.
#
# HINT:
# This step takes a long time.
# It takes the PRAW library about 1 second to "click" a link,
# and so it takes about 1 minute total to click all of them.
# I recommend saving this step for last since it will slow down your ability to run the steps below considerably.
# Get those working, then come back here and get this working.
all = submission.comments.replace_more(limit=None)

# FIXME:
# Loop through all the top level comments to calculate:
# 1. The total number of non-deleted top level comments,
# 2. The total number of deleted top level comments,
# 3. The total number of comments sent by each user.
#    You should use a dictionary where the keys are the username and the values are the total number of comments.
amount_deleted_top = 0
amount_nondeleted_top = 0
amount_total_top = 0

for top_level_comment in submission.comments:
    amount_total_top+=1
    if top_level_comment.author:
        amount_nondeleted_top += 1
    else:
        amount_deleted_top += 1

print('top level comments =', amount_total_top)
print('Deleted top level comments =', amount_deleted_top)
print('Non-deleted top level comments =', amount_nondeleted_top)
print('='*40)
print('all comments')
print('='*40)

# FIXME:
# Repeat the calculations above,
# but do it for ALL comments,
# not just top level comments.
all_amount_deleted_top = 0
all_amount_nondeleted_top = 0
all_amount_total_top = 0
for comment in all:
    all_amount_total_top+=1
    if comment.author:
        all_amount_nondeleted_top += 1
    else:
        all_amount_deleted_top += 1

print('All comments =', all_amount_total_top)
print('Deleted all level comments =', all_amount_deleted_top)
print('Non-deleted all level comments =', all_amount_nondeleted_top)
print('='*40)
print('all comments')
print('='*40)