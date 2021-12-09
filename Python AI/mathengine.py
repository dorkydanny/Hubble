from nextcord.ext import commands
from nextcord.ext import *
import discord
import nextcord

import asyncio
import random
import json
from discord_components import *
from os import path
import json
bot = commands.Bot('!')

class FirstButton(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @nextcord.ui.button(label='Suprise!', style=nextcord.ButtonStyle.green)
    async def clickit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'{ctx.author} hi', ephemeral=True)
        self.value = True
        self.stop()
    @bot.command()
    async def button(ctx):
        view=FirstButton()
    
    


bot.run('OTA1NTkxNTk0NDkxNzIzODE2.YYMT5Q.ieL1c5RvTa6_HANdDgz1HRBtr6w')