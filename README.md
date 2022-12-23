# Random picture

A Python script that prints the markdown for a painting selected from one of
several art-themed Twitter accounts.

The snippet is intended to be used in pull request descriptions.

## Install

Create a Python 3.10 virtualenv and run `make install`.

## Configure

Add Twitter credentials in a `config.py` module:

    TWITTER_CONSUMER_KEY = '...'
    TWITTER_CONSUMER_SECRET = '...'
    TWITTER_ACCESS_TOKEN_KEY = '...'
    TWITTER_ACCESS_TOKEN_SECRET  = '...'

and a list of Twitter usernames to select the image from:

    TWITTER_USERNAMES = (
        "HenryRothwell",
        "CanadaPaintings",
    )

## Run

Run:

    python main.py

which will print the markdown for a randomly selected image from one of the
configured Twitter accounts. E.g.

    [![🖼](http://pbs.twimg.com/media/FigqihhXgAAQaP6.jpg)](https://twitter.com/womensart1/status/1596573028334592000)
    <sub>— _Random painting (not related to content of PR)_</sub>"

which renders as:

[![🖼](http://pbs.twimg.com/media/FigqihhXgAAQaP6.jpg)](https://twitter.com/womensart1/status/1596573028334592000)<br/><sub>—
_Random painting (not related to content of PR)_</sub>

A `archive.json` file is used to ensure the same image isn't returned more than
once.
