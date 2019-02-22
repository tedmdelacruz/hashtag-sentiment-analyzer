# Hashtag Sentiment Analyzer

Analyzes the sentiments of a given hashtag using AWS Comprehend

Working demo http://bit.ly/HashtagSentimentAnalyzer

## Stack

- AWS Lambda for the serverless provider
- AWS Comprehend for retrieving the sentiment analysis
- [Serverless Framework](https://serverless.com) for developing and deploying the serverless application AWS Lambda

## Setup

```sh
npm install # Installs Serverless Framework and its dependencies
serverless deploy # Deploys the serverless application to AWS Lambda
sls deploy # Shorthand alias
sls remove # Removes the deployed stack
```
