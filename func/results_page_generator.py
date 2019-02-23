"""Generates a page for displaying the tweets with their respective sentiment
analysis results
"""
import boto3
import os
import logging
from dynamo_json import unmarshall
from jinja2 import Template

HASHTAG = os.environ['hashtag']
AWS_REGION = os.environ['aws_region']
STATIC_PAGE_BUCKET = os.environ['results_page_bucket']
ANALYZED_TWEETS_TABLE = os.environ['analyzed_tweets_table']
DEBUG = False

curr_path = os.path.dirname(os.path.realpath(__file__))
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(ANALYZED_TWEETS_TABLE)
    results = table.scan()
    if 'Items' not in results:
        logger.info('No items found')
        return

    tweets = results['Items']
    template_file = open(os.path.join(curr_path, 'tmpl', 'index.html'))
    template = Template(template_file.read())
    logger.info(tweets)
    rendered_page = template.render(hashtag=HASHTAG, tweets=tweets)

    if DEBUG:
        outfile_path = os.path.realpath(
            os.path.join(curr_path, 'rendered_page.html'))
        outfile = open(outfile_path, 'w')
        outfile.write(rendered_page)
        print(f'Generated: {outfile_path}')
        return

    s3 = boto3.client('s3', region_name=AWS_REGION)
    s3.put_object(
        Bucket=STATIC_PAGE_BUCKET,
        Body=rendered_page,
        ContentType='text/html',
        Key='index.html'
    )
