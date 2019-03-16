# Chap02-03/twitter_streaming.py
import sys
import string
import time
import json
import datetime
import tweepy
from tweepy import Cursor
from client import get_twitter_auth


def out_file_name():
    now = datetime.datetime.now()

    day = now.day
    month = now.month
    year = now.year

    return "downloads/backup_from_date_{}-{}-{}.jsonl".format(day, month, year)


if __name__ == '__main__':
    user_ids = ['158342368', '2288138575', '68740712', '50982086', '523386042',
                '20509689', '108994652', '19028805', '260788584', '2201623465']

    auth = get_twitter_auth()
    api = tweepy.API(auth)

    out_file = out_file_name()

    with open(out_file, 'w') as f:
        for user_id in user_ids:
            print(user_id)
            for page in Cursor(api.user_timeline, user_id=user_id).pages():
                for status in page:
                    data = json.dumps(status._json)
                    f.write(data)
