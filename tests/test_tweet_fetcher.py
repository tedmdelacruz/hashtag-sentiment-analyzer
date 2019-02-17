import os
from unittest import TestCase
from func import tweet_fetcher

class TestTweetFetcher(TestCase):

    def setUp(self):
        pass
    
    def test_lambda_handler(self):
        tweets = tweet_fetcher.lambda_handler({}, {})
        import ipdb; ipdb.set_trace()
