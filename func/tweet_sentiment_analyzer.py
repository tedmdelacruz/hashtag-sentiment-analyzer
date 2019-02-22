"""Listens to INSERT events in the fetched_tweets_table DynamoDB stream for new
tweet records and then runs each tweet into AWS Comprehend for
sentiment analysis. Writes the results into the analyzed_tweets_table.
"""
import boto3
import json
import logging
import os
import json
from dynamo_json import unmarshall

AWS_REGION = os.environ['aws_region']
ANALYZED_TWEETS_TABLE = os.environ['analyzed_tweets_table']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    if 'Records' not in event:
        logger.info('No records found')
        return

    comprehend = boto3.client(service_name='comprehend',
        region_name=AWS_REGION)

    results = []
    for record in event['Records']:
        if 'NewImage' not in record['dynamodb']:
            logger.info(record['dynamodb'])
            continue

        tweet = unmarshall(record['dynamodb']['NewImage'])
        text = tweet['text']
        result = comprehend.detect_sentiment(Text=text,
            LanguageCode='en')
        logger.info(f'Analyzed tweet: "{text}"')
        logger.info(f'Analysis results: {result}')
        tweet['sentiment'] = result['Sentiment']
        results.append(tweet)
    
    if not results:
        logger.info('No records analyzed')
        return

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(ANALYZED_TWEETS_TABLE)
    with table.batch_writer() as batch:
        for analyzed_tweet in results:
            batch.put_item(Item=analyzed_tweet)
