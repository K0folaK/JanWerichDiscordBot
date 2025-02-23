import os
import discord

def start_discord_bot():
    token = os.getenv("DISCORD_TOKEN")
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith("!ping"):
            await message.channel.send("Pong!")

    client.run(token)