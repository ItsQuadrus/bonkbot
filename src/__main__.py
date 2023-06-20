import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
import json
import datetime

load_dotenv()

player_types = {
    "classic": "quick_classic",
    "arrows": "quick_arrows",
    "grapple": "quick_grapple",
    "custom": "custom",
    "simple": "quick_simple",
    "total": "total"
}
first_player_types = {key: value.split("_")[0] for key, value in player_types.items()}
available_types = ", ".join(first_player_types.keys())
print(first_player_types)

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="!")
game = discord.Game("Bonk.io")
# Event that runs when the bot is ready
@bot.event
async def on_ready():
    print("BonkBot v.0.0.1")
    print("Bot is ready and online!")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def status(ctx, type: str = None):
    if type is None:
        # If no player type is specified, display the player count data in an embed
        playercount = requests.get("https://bonk2.io/scripts/combinedplayercount.txt")
        parse = playercount.text
        data = json.loads(parse)
        utc_now = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S UTC") # Get the current time in UTC

        # Create the embed
        embed = discord.Embed(title="Bonk.io Player count", description=f"Data as of {utc_now}", color=0x00ff00)

        # Add fields to the embed
        for key, value in zip(first_player_types.keys(), data["bonk"].values()):
            embed.add_field(name=key, value=value, inline=True)

        # Send the embed to the channel
        await ctx.send(embed=embed)
    else:
        # If a player type is specified, display the corresponding player count message
        try:
            key = player_types[type]
        except KeyError: # If the user enters an invalid player type, send an error message
            await ctx.send(f"Type invalid. Available player types: {available_types}")
            return

        playercount = requests.get("https://bonk2.io/scripts/combinedplayercount.txt")
        parse = playercount.text
        data = json.loads(parse)
        value = data["bonk"][key] # Get the value for the specified type that the user requested
        await ctx.send(f"There's {value} players online in {type}.") # Send the value to the channel, along with the type

bot.run(os.getenv("TOKEN"))


