"""Implements all functions related to reddit"""

import time
import asyncpraw
import asyncprawcore
import os
from dotenv import load_dotenv
import mangalist

SUBREDDIT = "Manga"

# Checks if post title matches correct format ([DISC] Title - Ch.xx or [DISC] Title :: Ch.xx) and is in manga list
def valid_title(title):
    print(f"{title}\n")

    split = title.upper().split(' ', 1)
    if len(split) <= 1:
        return False
    first_word = split[0]
    rest = split[1]

    if first_word == "[DISC]":
        post_title = rest.split(' -', 1)[0].split(' ::')[0]
        print(post_title)
        if post_title in mangalist.mangas:
            return True
    
    return False


# Searches through all new posts in the subreddit
async def search_subreddit(channel):
    load_dotenv()

    # Get reddit instance
    reddit = asyncpraw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="MangaBot",
        username="",
        password="",
    )

    print("running\n")

    # Load list of mangas
    mangalist.load_manga()
    
    # Get stream of new posts from subreddit
    subreddit = await reddit.subreddit(SUBREDDIT)
    searching = True
    while searching:
        try:
            async for submission in subreddit.stream.submissions(skip_existing=True):
                # Check if post title is in manga list
                if valid_title(submission.title):
                    # Post link in discord
                    print("Sending\n")
                    await channel.send(f"https://www.reddit.com{submission.permalink}")
        except asyncprawcore.AsyncPrawcoreException:
            time.sleep(10)

