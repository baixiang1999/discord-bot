from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests

import discord
import json
import time
import asyncio
from discord.ext import commands

with open("setting.json", mode="r", encoding="utf-8") as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()
# intents設定
# discordpy.readthedocs.io/en/stable/api.html#discord.Intents
# 例如要開啟成員變動事件
#intents.members = True
bot = commands.Bot(command_prefix="~", intents=intents)


while True:
    @bot.event  # 當機器人啟動
    async def on_ready():
        print("我出現ㄌ!")

    @bot.event  # 當有成員加入
    async def on_member_join(member):
        print(f"{member} join meow!")

    @bot.event  # 當有成員退出
    async def on_member_remove(member):
        print(f"{member} leave meow!")  # member=使用者名稱

    @bot.command()  # 查ping、ctx
    async def ping(ctx):  # 當收到!meow ping指令、ctx使用者輸入各項資料
        await ctx.send(f"{round(bot.latency*1000)} m/s")  # 機器人ping

    @bot.command()  # 傳送文字、圖片、本基圖片、取得ctx channnelID
    async def ttry(ctx):
        channel = bot.get_channel(ctx.channel.id)  # 取得使用者輸入文字的頻道ID
        await channel.send("meow")  # 傳送文字
        pic = discord.File(jdata["localPicture"])  # 指定discord檔案路徑
        await channel.send(file=pic)  # 傳送檔案
        await channel.send("https://reurl.cc/jGk5Mm")

    @bot.command()  # 無用
    async def job(ctx):
        channel = bot.get_channel(ctx.channel.id)
        await channel.send("https://reurl.cc/rRQ8dZ")

    @bot.command()
    async def test(ctx):  # 如果現在是17:50

        t = time.localtime()
        fmt = "%H:%M"
        now = time.strftime(fmt, t)
        if now == "17:50":
            await ctx.send(f"{now}")
        else:
            pass

    @bot.command()  # 機器人加入語音頻道
    async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @bot.command()  # 機器人退出語音頻道
    async def leave(ctx):
        await ctx.voice_client.disconnect()

    @bot.command()  # 無用爬蟲
    async def meow(ctx):
        channel = bot.get_channel(ctx.channel.id)
        searchText = ctx.message.content[6:]
        GetURL = "https://www.google.com.tw/search?q=" + searchText + \
            "&sxsrf=ALiCzsbUu0ELAOG2zFkgq4PRvIrTdWWqkQ:1659959922429&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjm6JHMmLf5AhX7x4sBHTM2AmsQ_AUoA3oECAEQBQ"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(GetURL, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        divSearch1 = soup.find_all(
            'img', limit=2)
        await channel.send(divSearch1[1].get("src"))

    bot.run(jdata['TOKEN'])
