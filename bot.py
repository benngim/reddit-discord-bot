"""Implementation of discord bot"""

import discord
import reddit
import os
from dotenv import load_dotenv


def run_discord_bot():
    load_dotenv(".env")
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!!\n")
        channel = client.get_channel(int(os.getenv("CHANNEL_ID")))
        await reddit.search_subreddit(channel)

    @client.event
    async def on_message(message):
        channel = client.get_channel(int(os.getenv("CHANNEL_ID")))

        # Message is sent by bot
        if message.author == client.user:
            return

        # Message is not from bot channel
        if message.channel != channel:
            return

        # Add new anime to animelist
        if message.content.startswith("!add-a"):
            print("!add anime command activated\n")
            split = message.content.split(' ', 1)
            if len(split) <= 1:
                print("Incorrect usage of add anime command\n")
                await channel.send("``Anime title must be submitted when using this command!``")
                return
            anime = split[1]
            added = reddit.animelist.add_anime(anime)
            if added:
                print(f"{anime.upper()} added to animelist\n")
                await channel.send(f"``{anime.upper()} has been successfully added to animelist!``")
            else:
                print(f"{anime.upper()} already in animelist\n")
                await channel.send(f"``{anime.upper()} is already in the animelist!``")

        # Add new manga to mangalist
        elif message.content.startswith("!add-m"):
            print("!add manga command activated\n")
            split = message.content.split(' ', 1)
            if len(split) <= 1:
                print("Incorrect usage of add manga command\n")
                await channel.send("``Manga title must be submitted when using this command!``")
                return
            manga = split[1]
            added = reddit.mangalist.add_manga(manga)
            if added:
                print(f"{manga.upper()} added to mangalist\n")
                await channel.send(f"``{manga.upper()} has been successfully added to mangalist!``")
            else:
                print(f"{manga.upper()} already in mangalist\n")
                await channel.send(f"``{manga.upper()} is already in the mangalist!``")

        # Display animes in animelist
        elif message.content.startswith("!animelist"):
            print("!animelist command activated\n")
            await channel.send(f"```ANIMELIST:\n{reddit.animelist.get_animelist()}```")

        # Deletes new anime from animelist
        elif message.content.startswith("!delete-a"):
            print("!delete anime command activated\n")
            split = message.content.split(' ', 1)
            if len(split) <= 1:
                print("Incorrect usage of delete anime command\n")
                await channel.send("``Anime title must be submitted when using this command!``")
                return
            anime = split[1]
            deleted = reddit.animelist.delete_anime(anime)
            if deleted:
                print(f"{anime.upper()} deleted from animelist\n")
                await channel.send(f"``{anime.upper()} has been successfully deleted from the animelist!``")
            else:
                print(f"{anime.upper()} already not in animelist\n")
                await channel.send(f"``{anime.upper()} is already not in animelist!``")

        # Deletes new manga from mangalist
        elif message.content.startswith("!delete-m"):
            print("!delete manga command activated\n")
            split = message.content.split(' ', 1)
            if len(split) <= 1:
                print("Incorrect usage of delete manga command\n")
                await channel.send("``Manga title must be submitted when using this command!``")
                return
            manga = split[1]
            deleted = reddit.mangalist.delete_manga(manga)
            if deleted:
                print(f"{manga.upper()} deleted from mangalist\n")
                await channel.send(f"``{manga.upper()} has been successfully deleted from the mangalist!``")
            else:
                print(f"{manga.upper()} already not in mangalist\n")
                await channel.send(f"``{manga.upper()} is already not in mangalist!``")

        # Display help message
        elif message.content.startswith("!help"):
            print("!help command activated\n")
            await channel.send(
                "```COMMANDS:\n" 
                + "!add-a [Anime] - Adds anime to bot's animelist\n"
                + "!add-m [Manga] - Adds manga to bot's mangalist\n"
                + "!animelist - Displays all anime in bot's animelist\n"
                + "!delete-a [Anime] - Deletes anime from bot's animelist\n"
                + "!delete-m [Manga] - Deletes manga from bot's mangalist\n"
                + "!help - Displays usage for bot commands\n"
                + "!mangalist - Displays all manga in bot's mangalist```"
                )

        # Display mangas in mangalist
        elif message.content.startswith("!mangalist"):
            print("!mangalist command activated\n")
            await channel.send(f"```MANGALIST:\n{reddit.mangalist.get_mangalist()}```")

        # Command not found
        else:
            print("Invalid command used\n")
            await channel.send("``Use !help for info on using this bot``")
            

    client.run(os.getenv("DISCORD_TOKEN"))



if __name__ == '__main__':
    run_discord_bot()
