import discord
from discord.ext import commands
intents = discord.Intents.all()
# intents設定
# discordpy.readthedocs.io/en/stable/api.html#discord.Intents
# 例如要開啟成員變動事件
#intents.members = True
bot = commands.Bot(command_prefix="!meow ", intents=intents)

while True:
    @bot.event
    async def on_ready():
        print("我出現ㄌ!")

    @bot.event
    async def on_member_join(member):
        print(f"{member} join meow!")

    @bot.event
    async def on_member_remove(member):
        print(f"leave meow!")

    @bot.command()  # 當收到!meow ping指令
    async def ping(ctx):
        await ctx.send(f"{round(bot.latency*1000)} m/s")

    @bot.command()
    async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @bot.command()
    async def leave(ctx):
        await ctx.voice_client.disconnect()

    token = "MTAwNDk4NjQ4MDI2OTE5NzMyMg.G7RAmA.y5xI1ff1WhXZnfE5fUb-x4fGDyOwVr5QNtNo94"
    bot.run(token)
