fake_tweets = [
    {
        'tweet_id': '9011283109283',
        'author': 'John Doe',
        'handle': 'jdoe123123123',
        'text': 'What a nice weather!',
        'url': 'https://twitter.com/9011283109283'
    },
    {
        'tweet_id': '81724919247',
        'author': 'Jane Doe',
        'handle': 'janedoe123123123',
        'text': 'I hate this traffic!',
        'url': 'https://twitter.com/81724919247'
    },
    {
        'tweet_id': '871287819431',
        'author': 'Juan dela Cruz',
        'handle': 'jdelacruz1827489174',
        'text': 'Look at this dog',
        'url': 'https://twitter.com/871287819431'
    }
]

fake_insert = {
    'Records': [
        {
            'dynamodb': {
                'NewImage': {
                    'tweet_id': {'N': '9011283109283'},
                    'author': {'S': 'John Doe'},
                    'handle': {'S': 'jdoe123123123'},
                    'text': {'S': 'What a nice weather!'},
                    'url': {'S': 'https://twitter.com/9011283109283'}
                },
            },
        },
        {
            'dynamodb': {
                'NewImage': {
                    'tweet_id': {'N': '81724919247'},
                    'author': {'S': 'Jane Doe'},
                    'handle': {'S': 'janedoe123123123'},
                    'text': {'S': 'I hate this traffic!'},
                    'url': {'S': 'https://twitter.com/81724919247'}
                },
            },
        },
        {
            'dynamodb': {
                'NewImage': {
                    'tweet_id': {'N': '871287819431'},
                    'author': {'S': 'Juan dela Cruz'},
                    'handle': {'S': 'jdelacruz1827489174'},
                    'text': {'S': 'Look at this dog'},
                    'url': {'S': 'https://twitter.com/871287819431'}
                },
            },
        },
    ]
}