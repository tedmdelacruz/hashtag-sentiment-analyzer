import os
from unittest import TestCase
from tests.fake_data import fake_insert_event

os.environ['aws_region'] = 'foo-region'
os.environ['analyzed_tweets_table'] = 'foo_analyzed_tweets'
from func import tweet_sentiment_analyzer

class TestTweetSentimentAnalyzer(TestCase):

    def test_lambda_handler(self):
        pass
        # tweet_sentiment_analyzer.lambda_handler(fake_insert_event, {})
