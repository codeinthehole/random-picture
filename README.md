# Random picture

A Python script that prints the markdown for a picture selected from one of
several art-themed Twitter accounts.

## Install

Create a virtualenv and run `make install`.

Add Twitter credentials in a `config.py` module:

    TWITTER_CONSUMER_KEY = '...'
    TWITTER_CONSUMER_SECRET = '...'
    TWITTER_ACCESS_TOKEN_KEY = '...'
    TWITTER_ACCESS_TOKEN_SECRET  = '...'

## Run

Run:

    python main.py

which will print the markdown for a randomly selected image from an arty Twitter
feed. E.g.

    [![](http://pbs.twimg.com/media/FigqihhXgAAQaP6.jpg)](https://twitter.com/womensart1/status/1596573028334592000)

which renders as:

[![](http://pbs.twimg.com/media/FigqihhXgAAQaP6.jpg)](https://twitter.com/womensart1/status/1596573028334592000)
