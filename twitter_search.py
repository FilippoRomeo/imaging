import os
import tweepy
import emoji
import re
import requests


def get_data(x):
        class obj : 
            def __init__(self, content, status_code):
                self.content = content
                self.sc = status_code
        return obj(requests.get(x).content, requests.get(x).status_code)
        

def twsejs(lat, lon):

    # read configs
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # api_key = config['twitter']['api_key']
    # api_key_secret = config['twitter']['api_key_secret']
    # access_token = config['twitter']['access_token']
    # access_token_secret = config['twitter']['access_token_secret']

    

    
    api_key = os.environ.get('API_KEY', None)
    api_key_secret = os.environ.get('API_KEY_SECRET', None)
    access_token = os.environ.get('ACCESS_TOKEN', None)
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET', None)

    # authentication
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    keywords = "love"
    data = []
    limit = 30

    # closest_loc = api.closest_trends(lat, lon)
    # trends = api.get_place_trends(closest_loc[0]['woeid'])

    # print(trends)

    def removeemoji(text):
        return emoji.get_emoji_regexp().sub(r'', text)

    def removelink(text):
        return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)


#  # if len(tweet.full_text) <= 50:
#     if bool(emoji.get_emoji_regexp().search(tweet.full_text)) or re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.full_text):
#         tweet.full_text = removeemoji(removelink(tweet.full_text))  
        
#         if any(obj['user'] == tweet.user for obj in data):
#                 pass

#         if tweet.retweeted or 'RT' or '@' in tweet.full_text:
#             pass
        
#         else: 
#             info = (tweet.full_text[:20] + '..') if len(tweet.full_text) > 20 else tweet.full_text
#             data.append({ "user" : str(tweet.user.screen_name), "tweet": str(info)})

  

    # for tweet in tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit):

    for tweet in tweepy.Cursor(api.search_tweets,q='*',geocode=("{},{},50mi").format(lat,lon), count=100,result_type="recent", tweet_mode='extended').items(limit):
        if len(tweet.full_text) <= 100:
            if bool(emoji.get_emoji_regexp().search(tweet.full_text)) or re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.full_text):
                tweet.full_text = removeemoji(removelink(tweet.full_text))  
            if any(obj['tweet'] == tweet.full_text for obj in data):
                pass
            else: 
                data.append({ "user": str(tweet.user.screen_name), "tweet": str(tweet.full_text)})
        # if len(data) == 10:
        #     break

    return data

if __name__ == '__main__':
    twsejs()