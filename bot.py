import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='VB!')

@bot.event()
async def on_ready(ctx):
    print('Logged in as')
    print(bot.user)
    print(bot.userid)
    print('---------')
    
@bot.command()
async def updates(ctx):
    embed=discord.Embed(title="Updates", description="This shows all recent updates", color=0xedfb40)
    embed.add_field(name="Update 0.01", value="Bot starting", inline=True)
    embed.set_footer(text="This bot was made by WolfBane#5559")
    await ctx.send(embed=embed)
    
bot.run('NDcyMjcxMTA2MTMzNDU4OTQ0.Djw-nQ.mv8x4GYWOwAzSqE_N1C2C66N9rA')
