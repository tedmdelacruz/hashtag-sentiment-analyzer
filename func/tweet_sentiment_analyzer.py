import boto3
import json
import logging
import os
from dynamo_json import unmarshall

AWS_REGION = os.environ['aws_region']
ANALYZED_TWEETS_TABLE = os.environ['analyzed_tweets_table']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    comprehend = boto3.client(service_name='comprehend',
        region_name=AWS_REGION)

    results = []
    for record in event['Records']:
        tweet = unmarshall(record['dynamodb']['NewImage'])
        text = tweet['text']
        result = comprehend.detect_sentiment(Text=text,
            LanguageCode='en')
        tweet['analysis_results'] = result
        logger.info(f'Analyzed tweet: "{text}"')
        logger.info(f'Analysis results: {result}')
        results.append(tweet)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(ANALYZED_TWEETS_TABLE)
    with table.batch_writer() as batch:
        for analyzed_tweet in results:
            batch.put_item(Item=analyzed_tweet)   
