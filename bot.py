import discord
from discord.ext import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
client = commands.Bot(command_prefix = "."
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("こんばんは"):
        if client.user != message.author:
            m="こんばんは" + message.author.name + "さん！"
            await message.channel.send(m)
    if message.content.startswith("こんにちは"):
        if client.user != message.author:
            m="こんにちは" + message.author.name + "さん！"
            await message.channel.send(m)
    if message.content.startswith("雑魚"):
        if client.user != message.author:
            m="お前が雑魚だよ" + message.author.name + "さん！"
            await message.channel.send(m)
    if message.content.startswith("死ね"):
        if client.user != message.author:
            m="お前が死ねよ" + message.author.name + "さん！"
            await message.channel.send(m)
    
client.run("NjEwMjAxODI2NDczNjcyNzYz.XVHa0Q.ON4OZxQzBpX2GEl8ViBO-bvmeC4")
