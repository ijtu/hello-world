import asyncio
import certifi
import discord
from discord.ext import commands
import os

os.environ["SSL_CERT_FILE"] = certifi.where()

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Hello World is now ready for use!")
    print("-----------------------------")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

spamming = False

@client.command()
async def helloworld(ctx):
    global spamming
    if not spamming:
        spamming = True
        while spamming:
            await ctx.send("Hello World!")
            await asyncio.sleep(2)
    else:
        await ctx.send("Already hello worlding")

@client.command()
async def stop(ctx):
    global spamming
    if spamming:
        spamming = False
        await ctx.send("Stopped hello worlding")
    else:
        await ctx.send("Not currently hello worlding")

@client.tree.command(name="hello", description="Say hi!")
async def hello(interaction):

    await interaction.response.send_message(f"Hey {interaction.user.mention}!")
        
client.run("MTIyMDA2NjMyMjgzMTExODQxNg.Gtotoe.IYrm64qZlHhbJO5oCLELXJP2VSqg-XipmzutLk")