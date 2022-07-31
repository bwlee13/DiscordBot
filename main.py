import requests
import discord
import time

"""
This BOT file will have to run client.run(token) at all times for Bot to be active

Bot commands and functions
# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#
"""

""" Get/Set Token and Set Client event """


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = discord.Client()


"""Bot Functionality - Add new functionality below"""


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Here are some useful commands. These only work in channel: general_dev")
        embed.add_field(name="!hello bot", value="Bot says Hi")
        await message.channel.send(content=None, embed=embed)

    if message.channel.name == 'general_dev':

        if message.content == "!hello bot":
            await message.channel.send(f"Hi there, {username}")


"""Un-comment client.run(token) and run script for bot to activate"""
client.run(token)

