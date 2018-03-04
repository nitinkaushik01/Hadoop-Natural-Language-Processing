

"""
Created on Thu Feb 15 21:31:04 2018

@author: Nitin
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import Sentiment_module as sent
from twitterkeys import *

#consumer key, consumer secret, access token, access secret.
consumerkey = consumerkey
consumersecret = consumersecret
access_token = access_token
access_secret = access_secret



class listener(StreamListener):

    def on_data(self, data):
        try:
            tweets_data = json.loads(data)

            tweet = tweets_data["text"]
            sentiment_value = sent.find_sentiment(tweet)
            print(tweet, sentiment_value)

            output = open("F:/output.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Nike"])


