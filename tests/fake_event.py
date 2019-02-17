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