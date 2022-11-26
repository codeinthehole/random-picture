import json
import os
import random
from typing import Iterator, List, Set, Tuple

import twitter  # type: ignore

import config


def random_image_markdown(
    twitter_client: twitter.Api,
    usernames: Tuple[str],
) -> str:
    """
    Return a markdown string for a random image.
    """
    img_url, tweet_url = _fetch_random_image(twitter_client, usernames)
    return f"[![]({img_url})]({tweet_url})"


def _fetch_random_image(
    client: twitter.Api, usernames: Tuple[str, ...]
) -> Tuple[str, str]:
    """
    Return the image URL and tweet URL for a random image from the passed accounts.
    """
    # Shuffle the Twitter accounts we look at.
    shuffled_usernames = list(usernames)
    random.shuffle(shuffled_usernames)

    # Loop through the first 200 tweets to find a picture we haven't used before.
    for username in shuffled_usernames:
        for status, image_urls in _image_tweets(client, username):
            if not _has_tweet_been_used_before(status):
                _record_tweet_use(status)
                return (
                    image_urls.pop(),
                    f"https://twitter.com/{username}/status/{status.id}",
                )

    raise RuntimeError("No image tweets found")


def _image_tweets(
    client: twitter.Api, username: str
) -> Iterator[Tuple[twitter.Status, Set[str]]]:
    """
    Return an iterator of tweets that have linked images.
    """
    max_id = None
    while True:
        statuses = client.GetUserTimeline(
            screen_name=username, max_id=max_id, count=200
        )
        # Break the loop once we run out of pages.
        if len(statuses) <= 1:
            return
        for status in statuses:
            # Fetch images linked to tweet.
            image_urls = set(_image_urls(status))
            if image_urls:
                yield status, image_urls
            max_id = status.id


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


# Archive utils


ARCHIVE_FILEPATH = "archive.json"


def _has_tweet_been_used_before(status: twitter.Status) -> bool:
    used_ids = _load_used_tweet_ids()
    return status.id in used_ids


def _record_tweet_use(status: twitter.Status) -> None:
    used_ids = _load_used_tweet_ids()
    used_ids.append(status.id)
    _save_used_tweet_ids(used_ids)


def _load_used_tweet_ids() -> List[str]:
    if os.path.exists(ARCHIVE_FILEPATH):
        with open(ARCHIVE_FILEPATH, "r") as f:
            return json.load(f)
    return []


def _save_used_tweet_ids(tweet_ids: List[str]) -> None:
    with open(ARCHIVE_FILEPATH, "w") as f:
        return json.dump(tweet_ids, f)


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


if __name__ == "__main__":
    print(
        random_image_markdown(
            twitter_client=_twitter_client(),
            usernames=config.TWITTER_USERNAMES,
        )
    )
