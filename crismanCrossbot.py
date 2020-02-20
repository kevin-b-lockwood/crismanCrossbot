# Kevin Lockwood

import os
import discord

###############################################################
# Get your token and put it in an otherwise empty file titled #
#                                                             #
#                        "token.txt"                          #
###############################################################
client = discord.Client()

with open("keywords.txt", "r") as keyword_file:
    keywords = keyword_file.readlines()

for i in range(len(keywords)):
    keywords[i] = keywords[i].strip()

print(keywords)

@client.event
async def on_message(message):
    has_sent = False
    for x in keywords:
        if (message.content.lower().count(x.lower()) > 0 and has_sent == False and message.author.name != "crismanCrossbot"):
            channel = message.channel
            await channel.send("You said `%s`, which reminds me: Crisman Crossing is the longest clear-span timber  truss bridge in the contiguous USA" % x)
            has_sent = True


with open("token.txt") as token_file:
    token = token_file.read()
    client.run(token)
