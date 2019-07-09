@client.event
async def on_message(message):
    if message.content.lower().startswith('!help'):
        commands = {}
        commands['&Owner'] = 'Shows who is the Owners of the Test1'
        commands['&Invite'] = 'Type &Invite Gives you a link to inv the bot to Your server!'
        commands['&Kick'] = 'Type &Kick @mention'
        commands['&purge'] = 'Type &purge <number>'
        commands['&Ban'] = "Type &Ban @mention"
        commands['&Say'] = 'Type &Say @mention to send to a friend a message'

        msg = discord.Embed(title='Test1',
                            description="Bot who gives shit.",
                            color=0x0000ff)
        for command, description in commands.items():
            msg.add_field(name=command, value=description, inline=False)
        msg.add_field(name='Join Ur Discord/For Questions/Chilling', value='https://discordapp.com/api/oauth2/authorize?client_id=597034304857440257&permissions=0&scope=bot', inline=False)
        await client.send_message(message.channel, embed=msg)
