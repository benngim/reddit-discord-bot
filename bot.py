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
        print(f"{client.user} is now running!!")
        channel = client.get_channel(config.CHANNEL_ID)
        await reddit.search_subreddit(channel)

    client.run(config.DISCORD_TOKEN)

    

    

    
    
if __name__ == '__main__':
    run_discord_bot()
