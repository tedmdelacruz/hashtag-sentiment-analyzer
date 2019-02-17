import boto3
import logging
import os
import random
from essential_generators import DocumentGenerator

FETCHED_TWEETS_TABLE = os.environ['fetched_tweets_table']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def random_tweet_generator():
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
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(FETCHED_TWEETS_TABLE)

    fetched_tweets = random_tweet_generator()
    logger.info(f'Fetched {len(fetched_tweets)} tweets...')
    with table.batch_writer() as batch:
        for tweet in fetched_tweets:
            batch.put_item(
                Item={
                    'tweet_id': random.randint(10000, 99999),
                    **tweet
                }
            )

