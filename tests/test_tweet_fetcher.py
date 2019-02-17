import os
from unittest import TestCase
from unittest.mock import MagicMock
from tests.fake_data import fake_tweets

os.environ['fetched_tweets_table'] = 'foo_fetched_tweets_table'
os.environ['hashtag'] = 'foo_hashtag'
from func import tweet_fetcher

class TestTweetFetcher(TestCase):

    def setUp(self):
        pass
    
    def test_lambda_handler(self):
        tweet_fetcher.get_tweets = MagicMock(return_value=fake_tweets)
        fake_dynamodb = MagicMock()
        tweet_fetcher.boto3.resource = MagicMock(return_value=fake_dynamodb)
        fake_table = MagicMock()
        fake_batch = MagicMock()
        fake_table.batch_writer = MagicMock(return_value=fake_batch)
        fake_dynamodb.Table = MagicMock(return_value=fake_table)

        tweet_fetcher.lambda_handler({}, {})
        import ipdb; ipdb.set_trace() # @TODO
