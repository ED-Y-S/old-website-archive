import time
import praw

reddit = praw.Reddit('bot')
url = "https://old.reddit.com/r/BotTown/comments/qqn9j8/politician_to_miss_his_antivaccine_mandate_rally/"
submission = reddit.submission(url=url)

for i in range(1): # spam it for 1000000 times
    print('made a comment, i = ',i)
    submission.comments[0].reply('"I put the art in fart" \n— Elon Musk (@elonmusk) January 9, 2020')
    time.sleep(5) #let the bot "sleep" for 5 minutes