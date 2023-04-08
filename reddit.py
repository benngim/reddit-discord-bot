"""Implements all functions related to reddit"""

import time
import asyncpraw
import asyncprawcore
import os
from dotenv import load_dotenv
import mangalist
import animelist

SUBREDDIT1 = "Manga"
SUBREDDIT2 = "Anime"

# Checks if post title matches correct format for manga subreddit and is in manga list
def valid_manga_title(title):
    print(f"New Post (Manga):\n{title}\n")

    split = title.upper().split(' ', 1)
    if len(split) <= 1:
        return False
    first_word = split[0]
    rest = split[1]

    if first_word == "[DISC]":
        post_title = rest.split(' -', 1)[0].split(' ::')[0].split(' (Ch')[0].split(' Ch.')[0]
        if post_title in mangalist.mangas:
            return True
    
    return False

# Checks if post title matches correct format for anime subreddit and is in anime list
def valid_anime_title(title):
    print(f"New Post (Anime):\n{title}\n")

    post_titles = title.upper().split(' -', 1)[0].split(' • ', 1)
    for post_title in post_titles:
        if post_title in animelist.animes:
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

    # Load list of mangas
    mangalist.load_manga()

    # Load list of animes
    animelist.load_anime()
    
    # Get stream of new posts from subreddit
    subreddit = await reddit.subreddit(f"{SUBREDDIT1}+{SUBREDDIT2}")
    searching = True
    while searching:
        try:
            async for submission in subreddit.stream.submissions(skip_existing=True):
                # Post is from manga subreddit
                if submission.subreddit.display_name == SUBREDDIT1:
                    # Check if post title is in manga list
                    if valid_manga_title(submission.title):
                        # Post link in discord
                        print("Valid Post, sending to channel\n")
                        await channel.send(f"https://www.reddit.com{submission.permalink}")
                # Post is from anime subreddit
                else:
                    # Check if post title is in anime list
                    if valid_anime_title(submission.title):
                        # Post link in discord
                        print("Valid Post, sending to channel\n")
                        await channel.send(f"https://www.reddit.com{submission.permalink}")
        except asyncprawcore.AsyncPrawcoreException:
            time.sleep(10)

