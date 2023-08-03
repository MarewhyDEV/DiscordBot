import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {ctx.author}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')
@bot.command()
async def rulet(ctx):
    renkler = ["Kırmızı","Siyah","Yeşil"]
    secilen_renk = random.choices(renkler, weights=[48,48,4], k=1)[0]
    await ctx.send(secilen_renk)

bot.run("token")