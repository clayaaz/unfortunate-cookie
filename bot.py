import discord
from discord.ext import commands
from discord import app_commands
from random import randint
import api

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Syncing the slash command with Discord
    await bot.tree.sync()

@bot.command()
async def fortune(ctx):
    await ctx.send(api.returnFortune())

@bot.tree.command(name="fortune", description="Get a random fortune.")
async def fortune(interaction: discord.Interaction):
    await interaction.response.send_message(api.returnFortune())

bot.run("BOT_TOKEN")
