import GetOldTweets3 as got
from datetime import datetime
import pandas as pd
import csv

tweetlist = []

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('lufthansa')\
                                           .setSince("2019-12-30")\
                                           .setUntil(str(datetime.date(datetime.now())))\
                                           .setMaxTweets(12000)
                                           
if (len(got.manager.TweetManager.getTweets(tweetCriteria))!=0):
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for tweet in tweets:
        new = ((tweet.id,tweet.username ,datetime.date(tweet.date),tweet.retweets,tweet.text,tweet.geo))
        tweetlist.append(new)
    df = pd.DataFrame(tweetlist,columns=["id", "UserName", "date","retweets","text","geoloc"])
    df.to_csv('quoted.csv')    
    # print(json.dumps(tweet))
    

else:
    print("NaN")















    # with open('innovators.csv', 'w', newline='',encoding="utf-8") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["id", "UserName", "date","retweets","text"])
    #         writer.writerow([tweet.id,tweet.username ,tweet.date,tweet.retweets,tweet.text])