"""Tweet Fetcher

Periodically fetches tweets using specified hashtag and writes the tweets into
DynamoDB.
"""
import boto3
import logging
import os

# @FIXME
import random
from essential_generators import DocumentGenerator

FETCHED_TWEETS_TABLE = os.environ['fetched_tweets_table']
HASHTAG = os.environ['hashtag']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_tweets(hashtag):
    """Fetches tweets using the specified hashtag from Twitter API"""
    # @TODO Fix this once your Twitter Developer account has been approved
    gen = DocumentGenerator()
    template = {
        'url': 'url',
        'handle': 'word',
        'author': 'name',
        'text': 'sentence'
    }
    gen.set_template(template)
    return gen.documents(10)


def lambda_handler(event, context):
    fetched_tweets = get_tweets(HASHTAG)
    logger.info(f'Fetched {len(fetched_tweets)} tweets...')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(FETCHED_TWEETS_TABLE)
    with table.batch_writer() as batch:
        for tweet in fetched_tweets:
            batch.put_item(
                Item={
                    'tweet_id': random.randint(10000, 99999), # @FIXME
                    **tweet
                }
            )
