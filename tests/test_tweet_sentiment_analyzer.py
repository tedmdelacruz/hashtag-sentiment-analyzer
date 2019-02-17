import os
from unittest import TestCase
from tests import fake_event

os.environ['aws_region'] = 'ap-southeast-1'
os.environ['analyzed_tweets_table'] = 'analyzed_tweets'
from func import tweet_sentiment_analyzer

class TestTweetSentimentAnalyzer(TestCase):

    def setUp(self):
        pass
    
    def test_lambda_handler(self):
        tweet_sentiment_analyzer.lambda_handler(fake_event.fake_insert, {})
        pass
