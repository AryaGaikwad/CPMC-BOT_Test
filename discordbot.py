import discord
TOKEN = 'OTgwMzE0NDI0ODI3MDY0MzQw.GXRn_L.ZRhUtXcPat_3Kl-hkav52bJ8DE-jyLIXdILAtk'
client = discord.Client()

@client.event #registering to an event
async def on_ready(): #bot is ready and working
    print("We have logged in as {0.user}".format(client))

x=['hi','hello','Hello','HI']
@client.event  # registering to an event
async def on_message(message):  # bot is ready and working
    if message.author == client.user:
        return
    if message.content.startswith(tuple(x)):
        await message.channel.send('Hello!')


client.run(TOKEN)#to log in

