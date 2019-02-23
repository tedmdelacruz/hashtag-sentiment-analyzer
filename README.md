# Hashtag Sentiment Analyzer

Analyzes the sentiments of a given hashtag using AWS Comprehend

Working demo http://bit.ly/HashtagSentimentAnalyzer

![Architecture Diagram](./architecture.png)

## Stack

- [AWS Lambda](https://aws.amazon.com/lambda/) for the serverless computing provider
- [AWS Comprehend](https://aws.amazon.com/comprehend/) for retrieving the sentiment analysis
- [Serverless Framework](https://serverless.com) for developing and deploying the serverless application on AWS Lambda

## Setup

```sh
# Install Serverless Framework and its dependencies
npm install

# Deploy the serverless application to AWS Lambda
serverless deploy 

# Shorthand alias
sls deploy

# Removes the deployed stack
sls remove
```
