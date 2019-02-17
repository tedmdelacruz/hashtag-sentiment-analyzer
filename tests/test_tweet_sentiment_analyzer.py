import os
from unittest import TestCase

os.environ['aws_region'] = 'foo-region'
os.environ['analyzed_tweets_table'] = 'foo_analyzed_tweets'
from func import tweet_sentiment_analyzer

class TestTweetSentimentAnalyzer(TestCase):

    def setUp(self):
        pass
    
    def test_lambda_handler(self):
        pass
