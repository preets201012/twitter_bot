# tweepy-bots/bots/config.py
import tweepy
import logging
# from os import environ
import os

logger = logging.getLogger()


def create_api():
    # consumer_key = os.getenv("CONSUMER_KEY")
    # consumer_secret = os.getenv("CONSUMER_SECRET")
    # access_token = os.getenv("ACCESS_TOKEN")
    # access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # consumer_key = environ['CONSUMER_KEY']
    # consumer_secret = environ['CONSUMER_SECRET']
    # access_token = environ['ACCESS_TOKEN']
    # access_token_secret = environ['ACCESS_TOKEN_SECRET']

    consumer_key = os.environ.get('CONSUMER_KEY', None)
    consumer_secret = os.environ.get('CONSUMER_SECRET', None)
    access_token = os.environ.get('ACCESS_TOKEN', None)
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET', None)

    logger.info(consumer_key)
    logger.info(consumer_secret)
    logger.info(access_token)
    logger.info(access_token_secret)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
