# Imaging

 This website shows what appear to be 3d objecs with a glitch effect. It is a concept for a web installation of tweets based on the geolocation of the user that access it. Thanks to the data leaks such as geolocation, public ip address and so on we are able to give a position and the tweets that have been made around the user over a 5 mile area. It combine front end tech like Three.js and backend technology such as Flask python, The back end is necessary to make raquest, get data and secure keys from the public. Once the data is obtained is sent to the fron end as a json formats and js interacts with it. 

 ```bash
git clone https://github.com/FilippoRomeo/imaging
```
Sign in to the [twitter api](https://developer.twitter.com/en/docs/twitter-api), get the key and add em to the [twitter_search.py](https://github.com/FilippoRomeo/imaging/blob/main/twitter_search.py) file.
 ```bash
cd imaging
python3 app.py
```

Visit http://127.0.0.1:5000/

[View example on heroku](https://iamaging.herokuapp.com/)
 
If it doesn't start, please refresh the page. The server is on a free tier and is not always running.

API used are freeGeoIP.app and Tweepy python library for accessing the Twitter API. 

There might be a problem in running the application due being on heroku, free service that limit the requests. In cas it occours refresh the page.
