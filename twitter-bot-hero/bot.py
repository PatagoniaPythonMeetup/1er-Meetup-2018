import time
import tweepy
import os
from datetime import date

# Credentials

CONSUMER_KEY = 'lzCIVKmAk5dFz66bdLahARZi5'
CONSUMER_SECRET = 'PNsO3TRTbJVOHC7ukXpe6FnF3pr73ilOWQ8mAOGgvQ5sYF4d8d'
ACCESS_KEY = '969361386450112513-4Ce1pAaVYxYAscnXp6qxBNqnXScd3DI'
ACCESS_SECRET = 'gI2SRiOYr1e4JMKfZWhDMJUDabbCzplByjVE7CWpXH6u0'

# Aunticarse usando lo antes seteado
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
tweets = []
while True:
    for tweet in tweepy.Cursor(api.search,q="#patagonia #python #meetup -filter:retweets since:{}".format(date.today().strftime('%Y-%m-%d')),tweet_mode='extended').items():
        try:
            if tweet.id not in tweets:
                print(tweet.full_text)
                print(tweet.user.screen_name)
                tweets.append(tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(6)

