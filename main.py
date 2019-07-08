
import discord


TOKEN = 'NTk3MDM0MzA0ODU3NDQwMjU3.XSCNkg.gI9YzjTOwzz64jMaXZGvhibmo0k'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
