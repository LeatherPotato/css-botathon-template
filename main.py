import os
import discord
from discord import app_commands

from imported_command_example import imported_command

GUILD_ID = os.environ["GUILD_ID"]
TOKEN = os.environ["TOKEN"]

MY_GUILD = discord.Object(id=GUILD_ID) # enter guild id? this is how i do my bots but there *should* be a way to update it for all guilds its in, right?


class MyClient(discord.Client):
    
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


# commands go here

@app_commands.command(description="syncs the command tree manually, though the bot is set up to do this automatically on run.")
@client.tree.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
    # id reccomend you add some checks here to make sure only people with specific permissions can sync the command tree.
    await client.tree.sync()
    print('Command tree synced.')
    await interaction.response.send_message('Command tree synced.')

@app_commands.command(description="pings the bot and returns the latency")
@client.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'pong!! {round(client.latency, 1)}s')


# commands organised into other folders go here
client.tree.add_command(imported_command.ImportedCommand(client=client))

client.run(TOKEN)