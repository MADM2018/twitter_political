# Chap02-03/twitter_streaming.py
import sys
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from client import get_twitter_auth
import datetime


class CustomListener(StreamListener):
    """Custom StreamListener for streaming Twitter data."""

    def __init__(self, file_prefix):
        self.out_file_prefix = file_prefix

    def out_file_name(self):
        now = datetime.datetime.now()

        day = now.day
        month = now.month
        year = now.year

        return "downloads/{}_stream_from_date_{}-{}-{}.jsonl".format(self.out_file_prefix, day, month, year)

    def on_data(self, data):
        try:
            out_file = self.out_file_name()
            with open(out_file, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            sys.stderr.write("Error on_data: {}\n".format(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Rate limit exceeded{}\n".format(status))
            return False
        else:
            sys.stderr.write("Error {}\n".format(status))
            return True


if __name__ == '__main__':
    filter = {
        'follow': ['158342368', '2288138575', '68740712', '50982086', '523386042', '20509689', '108994652', '19028805', '260788584', '2201623465']
    }

    auth = get_twitter_auth()
    twitter_stream = Stream(auth, CustomListener('Spain_Political'))
    twitter_stream.filter(**filter)
