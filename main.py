import discord
from discord.ext import commands
from scraper.hanime import Hanime

client = commands.Bot(command_prefix="s.")
client.remove_command("help")

@client.event
async def on_ready():
  print("Online!")

@client.command()
async def poon(ctx):
  hanime = Hanime(config)
  hanime.run()
  for link in hanime.links:
    await ctx.send(link)

client.run("token here")
