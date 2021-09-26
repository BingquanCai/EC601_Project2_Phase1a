import tweepy #https://github.com/tweepy/tweepy
import json

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = "access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Get tweets of the user by timeline
#'count' can specify the number of tweets
public_tweets = api.user_timeline(id="BU_Tweets", count=5)

#Set a number before the printing tweets
i=1

#Print tweets of the user by timeline
for tweet in public_tweets:
    print(str(i)+'. '+tweet.text+'\n')
    i=i+1
