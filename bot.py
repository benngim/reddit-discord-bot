"""Implementation of discord bot"""

import discord
import reddit
import config


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!!\n")
        channel = client.get_channel(config.CHANNEL_ID)
        await reddit.search_subreddit(channel)

    @client.event
    async def on_message(message):
        channel = client.get_channel(config.CHANNEL_ID)

        # Message is sent by bot
        if message.author == client.user:
            return

        # Message is not from bot channel
        if message.channel != channel:
            return

        # Add new manga to mangalist
        if message.content.startswith("!add"):
            split = message.content.split(' ', 1)
            if len(split) <= 1:
                await channel.send("``Manga title must be submitted when using this command!``")
                return
            manga = split[1]
            added = reddit.mangalist.add_manga(manga)
            if added:
                await channel.send(f"``{manga.upper()} has been successfully added to mangalist!``")
            else:
                await channel.send(f"``{manga.upper()} is already in the mangalist!``")

        # Deletes new manga to mangalist
        elif message.content.startswith("!delete"):
            split = message.content.split(' ', 1)
            if len(split) <= 1:
                await channel.send("``Manga title must be submitted when using this command!``")
                return
            manga = split[1]
            deleted = reddit.mangalist.delete_manga(manga)
            if deleted:
                await channel.send(f"``{manga.upper()} has been successfully deleted from the mangalist!``")
            else:
                await channel.send(f"``{manga.upper()} is already not in mangalist!``")

        # Display help message
        elif message.content.startswith("!help"):
            await channel.send(
                "``` COMMANDS:\n !add [Manga] - Adds manga to bot's mangalist\n !delete [Manga] - Deletes manga from bot's mangalist\n !help - Displays usage for bot commands```"
                )

        # Command not found
        else:
            await channel.send("``Use !help for info on using this bot``")
            

    client.run(config.DISCORD_TOKEN)

    

    

    
    
if __name__ == '__main__':
    run_discord_bot()
