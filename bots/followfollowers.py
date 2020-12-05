#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in limit_handled(tweepy.Cursor(api.followers).items()):
        if not follower.following:
            try:
                logger.info(f"Following {follower.name}")
                follower.follow()
            except Exception as e:
                logger.error("Error during following", exc_info=True)

            time.sleep(60)


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(60 * 60)


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(300)


if __name__ == "__main__":
    main()
