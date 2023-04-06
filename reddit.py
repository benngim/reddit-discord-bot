"""Implements all functions related to reddit"""

import praw
import config

SUBREDDIT = "Manga"

# Checks if post title matches correct format and is in manga list
def valid_title(title):
    pass


# Searches through all new posts in the subreddit
def search_subreddit():
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent="MangaBot",
        username="",
        password="",
    )

    subreddit = reddit.subreddit(SUBREDDIT)
    for submission in subreddit.stream.submissions():
        # Check if post title is in manga list
        if valid_title(submission.title.upper()) {
            # Post link in discord

        }
