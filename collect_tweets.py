#!/usr/bin/env python

import sys
import json

sys.path.append("got")
from got.manager import TweetCriteria, TweetManager


QUERY_STRING = 'BrunoLatourAIME OR modesofexistence OR "modes of existence" OR url:"modesofexistence org" OR "Bruno Latour" OR brunolatour'
NB_TWEETS = 50


query = TweetCriteria().setQuerySearch(QUERY_STRING).setMaxTweets(NB_TWEETS)

tweets = []
for tweet in TweetManager.getTweets(query):
    tweets.append({
        "date": int(tweet.date.strftime("%s")),
        "id": long(tweet.id),
        "link": tweet.permalink,
        "message": tweet.text,
        "screenname": tweet.username
    })

if tweets:
    with open("tweets-aime.json", "w") as f:
        json.dump(tweets, f)
