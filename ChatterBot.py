# Dependencies
import numpy as np
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "j6UMJ9RL1s6IzP9bMuDF7aqs2"
consumer_secret = "A3oP0clXf60RzFHu9SkDtzzWRKr35sxZpKhP5RgM0CbAkwlXPa"
access_token = "979169660833710080-WiJS6293MQ0ejXeWjNaawSofVNskv53"
access_token_secret = "NIs5dvQRRXSLizsRrx4j6ATJX1JISdPudkXxYqBlpZ2dC"

# Target Term
target_term = "@kindredseekers"

# Opening message
print("We're going live!")

# Create Thank You Function
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=5, result_type="recent")

    # Loop through all tweets
    # Loop through all public_tweets
    for tweet in public_tweets["statuses"]:

        # Get ID and Author of most recent tweet directed to me
        tweet_id = tweet["id"]
        tweet_author = tweet["user"]["screen_name"]
        tweet_text = tweet["text"]

        # Print Tweet Text and Tweet Author
        print(tweet_text)
        print(tweet_author)
        
        try:
            api.update_status("Hey @"+tweet_author+"! You are a cool person!")
            print("Successful response!")
        except Exception:
            print("I ALREADY DID THAT ONE!")

ThankYou()

while(True):
    ThankYou()
    time.sleep(60)