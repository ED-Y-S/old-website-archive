import praw
reddit = praw.Reddit('bot') # Calling the username from the praw.ini

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/" # recommend old.reddit
submission = reddit.submission(url=url)

#submission.comments.replace_morw(limit=None) clicks all of the "more comments" so you get all of them

for top_level_comment in submission.comments:
    print('type(top_level_comment)=', type(top_level_comment)) #tell you the type of this file
    #if type(top_level_comment) == praw.models.reddit.comment.Comment:
    #    print(top_level_comment.body)
    try:
        print(top_level_comment.body) # .body is the comment as markdown
        
    except AttributeError:
        pass


#submission.comments[0].replies[1].replies[0].... multiple .replies
#submission.comments[0].replies[1].replies[0].authors to see the author
#submission.comments[0].replies[1].replies[0].parent()
#replace_comment() clicks all the 'more comments' so that you see all comments
#submissionm.comments.list() gives you a list of all comments(including non-top ones)
#list(submission.comments) coverts top comments into a list
