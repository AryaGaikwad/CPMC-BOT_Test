import discord
import aiohttp
import asyncio
TOKEN = 'OTgwMzE0NDI0ODI3MDY0MzQw.GXRn_L.ZRhUtXcPat_3Kl-hkav52bJ8DE-jyLIXdILAtk'
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event #registering to an event
async def on_ready(): #bot is ready and working
    print("We have logged in as {0.user}".format(client))

@client.command(name="hi")
async def user(ctx):
    await ctx.reply("HII")


@client.command()
async def name(ctx,name):
    await ctx.reply("HII  "+name)


@client.command()
async def mul(ctx,a:int,b:int):
    await ctx.reply(a*b)

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('') as response:
            print('status',response.status)
            data = await response.json()
            print('data: ' , data)

loop=asyncio.get_event_loop()
loop.run_until_complete(main())

client.run(TOKEN)
