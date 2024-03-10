import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def plastic(ctx):
    list_plas = ['Пластик можно переработать в красивую игрушку, например, сделать из пластиковой бутыки кормушку для птиц.', 'Пластик можно переплавить и сделать из него посуду для пищи.', 'Отрезав верхнюю часть пластиковой бутылки, можно сделать пенал, дополнительно украсив его']
    await ctx.send(random.choice(list_plas))

@bot.command()
async def metal(ctx):
    list_met = ['Любой металл можно отнести в пункты сдачи, даже получив за него вознаграждение.', 'Металл можно принести мастеру и он переплавит его во что-либо нужное.']
    await ctx.send(random.choice(list_met))

bot.run("")