"""
Usage:

    $ python main.py
"""
from typing import Iterator, Tuple

import twitter  # type: ignore

import config


def random_image_markdown() -> str:
    """
    Return a markdown string for a random image.
    """
    usernames = (
        "HenryRothwell",
        "womensart1",
        "ahistoryinart",
    )
    client = _twitter_client()

    img_url, tweet_url = _fetch_random_image(client, usernames)
    return f"[![]({img_url})]({tweet_url})"


def _twitter_client() -> twitter.Api:
    """
    Return a configured Twitter client.
    """
    return twitter.Api(
        consumer_key=config.TWITTER_CONSUMER_KEY,
        consumer_secret=config.TWITTER_CONSUMER_SECRET,
        access_token_key=config.TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET,
        tweet_mode="extended",
    )


def _fetch_random_image(
    client: twitter.Api, usernames: Tuple[str, ...]
) -> Tuple[str, str]:
    """
    Return the image URL and tweet URL for a random image.
    """
    # TODO track which images have been printed out before.
    for username in usernames:
        statuses = client.GetUserTimeline(screen_name=username, count=200)
        for status in statuses:
            image_urls = set(_image_urls(status))
            if image_urls:
                return (
                    image_urls.pop(),
                    f"https://twitter.com/{username}/status/{status.id}",
                )

    raise RuntimeError("No image tweets found")


def _image_urls(status: twitter.Status) -> Iterator[str]:
    """
    Return an iterator of tweet images.
    """
    # Loop over images in the entities/media list
    try:
        entities = status._json["entities"]["media"]
    except KeyError:
        pass
    else:
        for entity in entities:
            yield entity["media_url"]

    # Loop over images in the extended_entities/media list
    try:
        entities = status._json["extended_entities"]["media"]
    except KeyError:
        pass
    else:
        for entity in entities:
            yield entity["media_url"]


if __name__ == "__main__":
    print(random_image_markdown())
