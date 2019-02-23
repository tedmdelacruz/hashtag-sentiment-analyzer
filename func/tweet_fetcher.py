"""Periodically fetches tweets using specified hashtag and writes the tweets
into DynamoDB.
"""
import boto3
import logging
import os
import twitter

NUM_TWEETS = 50
FETCHED_TWEETS_TABLE = os.environ['fetched_tweets_table']
HASHTAG = os.environ['hashtag']

TWITTER_API_CONSUMER_KEY = os.environ['twitter_api_consumer_key']
TWITTER_API_ACCESS_TOKEN_KEY = os.environ['twitter_api_access_token_key']

ssm_client = boto3.client('ssm')
def get_secret(key):
    response = ssm_client.get_parameter(
        Name=key,
        WithDecryption=True
    )
    return response['Parameter']['Value']

TWITTER_API_CONSUMER_SECRET = get_secret('twitter_api_consumer_secret')
TWITTER_API_ACCESS_TOKEN_SECRET = get_secret('twitter_api_access_token_secret')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def format_tweet(tweet):
    """Formats twitter.Status models into desired format in DynamoDB"""
    user = tweet['user']
    return {
        'tweet_id': tweet['id'],
        'hashtag': HASHTAG,
        'text': tweet['text'],
        'created_at': tweet['created_at'],
        'user': {
            'user_id': user['id'],
            'name': user['name'],
            'handle': user['screen_name'],
            'profile_image_url': user['profile_image_url'],
            'profile_url': f"https://twitter.com/{user['screen_name']}"
        }
    }


def get_tweets(hashtag):
    """Fetch tweets using specified hashtag using Twitter API"""
    api = twitter.Api(consumer_key=TWITTER_API_CONSUMER_KEY,
                      consumer_secret=TWITTER_API_CONSUMER_SECRET,
                      access_token_key=TWITTER_API_ACCESS_TOKEN_KEY,
                      access_token_secret=TWITTER_API_ACCESS_TOKEN_SECRET)

    query = (f"q=%23{HASHTAG}%20-RT"
             f"&result_type=recent&since=2019-01-01&count={NUM_TWEETS}")
    results = api.GetSearch(raw_query=query)

    return [
        format_tweet(tweet.AsDict())
        for tweet in results
    ]


def lambda_handler(event, context):
    logger.info(f'Fetching tweets related to #{HASHTAG}...')
    fetched_tweets = get_tweets(HASHTAG)
    logger.info(f'Fetched {len(fetched_tweets)} tweets')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(FETCHED_TWEETS_TABLE)
    with table.batch_writer() as batch:
        for tweet in fetched_tweets:
            batch.put_item(Item=tweet)
