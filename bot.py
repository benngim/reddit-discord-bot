"""Implementation of discord bot"""

import discord
import config


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_start():
        print(f"{client.user} is now running!!")

    client.run(config.DISCORD_TOKEN)

    
    
if __name__ == '__main__':
    run_discord_bot()
