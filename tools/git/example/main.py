import subprocess

from discord.ext.commands import Bot
from constants import *

bot = Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Successfully logged in as: {bot.user}")


@bot.command()
async def update(ctx):
    await ctx.send("Updating!")
    subprocess.call(["sh", "./update.sh"])
    quit(0)


@bot.command()
async def test(ctx):
    await ctx.send("WORD UP!!")


if __name__ == '__main__':
    bot.run(DISCORD_BOT_TOKEN)
