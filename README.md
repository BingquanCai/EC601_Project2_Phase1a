# EC601_Project2_Phase1a

- 2021 Fall Boston University Class EC601 Project 2 Phase 1(a)

- Bingquan Cai

## Twitter & Twitter API

**Twitter** is a platform that provides real-time events and hot topics for discussion around the world today. On Twitter, real-time commentary conversations show every side of the story from breaking news, entertainment messages, sports news, political news, to everyday information in an all-encompassing way. Here, you can join open and real-time conversations or even watch live events.

The **Twitter API** can be used to programmatically retrieve and analyze data, as well as engage with the conversation on Twitter. This API provides access to a variety of different resources including the following: Tweets, Users, Direct Messages, Lists, Trends, Media, Places.

## Get Tweets of The User - by Timeline

In the [Twitter_API.py](https://github.com/BingquanCai/EC601_Project2_Phase1a/blob/main/Twitter_API.py) that I upload, I import **tweepy** to help me achieve the function I want to accomplish. **Tweepy** is a module designed to handle the Twitter API in Python in a fairly simple way.

I use `api.user_timeline()` to get tweets of the user by timeline. In the `api.user_timeline()`, I can type in the id of whomever I want and specify the number of tweets.

## Tests and Results

Here is the example that I use my [Twitter_API.py](https://github.com/BingquanCai/EC601_Project2_Phase1a/blob/main/Twitter_API.py) to get tweets of the user by timeline.

![online](https://raw.githubusercontent.com/BingquanCai/Pictures/main/BUTweets_online.jpg)

As you can see, when I get to the homepage of Boston University, I am not able to get multiple tweets from Boston University within the screen due to the screen size limitation.

![API](https://raw.githubusercontent.com/BingquanCai/Pictures/main/BUTweets.jpg)

If I type in the id of Boston University and set the count to 5, I will get 5 recent tweets from Boston University by timeline.
