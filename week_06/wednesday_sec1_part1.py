#triple quotation mark serves the sane functions as others, but it explicits serves muilti-lines
tweets = '''
    [  
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12
        
    }
]
    '''

import json
tweet_loads=json.loads(tweets)
# we now know how to load strings from files
# special type of file called of JSON files which contain pythjon code that can be loaded with the json.loads function

num_trump = 0
for tweet_load in tweet_loads:
    # if 'Trump' in tweet_loads['text'].lower():
    if tweet_load['text'].find('trump') != -1:
        num_trump += 1