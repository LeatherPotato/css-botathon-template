import discord
from discord import app_commands

class ImportedCommand(app_commands.Group):

    def __init__(self, client: discord.Client):
        super().__init__()
        self.client = client
    
    @app_commands.command(description="echoes back what you say")
    @app_commands.describe(message="message to be echoed back")
    async def echo(self, 
                   interaction: discord.Interaction,
                   message: str = ""):
        if message == "":
            return_string = "No message enterred!"
        else:
            return_string = f"The enterred message: {message}"
        await interaction.response.send_message(return_string)
