# Random picture

A Python script that prints the markdown for a random picture selected from a
art-themed Twitter account.

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
