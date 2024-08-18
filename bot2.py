{\rtf1\ansi\ansicpg936\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import json\
from itertools import product\
import discord\
from discord import ApplicationContext, Bot, Message, DMChannel, PartialMessageable\
\
\
def run(bot: Bot):\
    # \uc0\u22312 \u36825 \u37324 \u28155 \u21152 \u20320 \u30340  bot.run('YOUR_BOT_TOKEN')\
    token = \'93\'94\
    bot.run(token)\
\
\
def main():\
    bot = discord.Bot(intents=discord.Intents.all())\
\
    @bot.event\
    async def on_ready():\
        print(f"\{bot.user\} is ready and online!")\
\
    @bot.slash_command(name="buy", description="Long or short a coin with specific amount")\
    async def monitor(ctx: ApplicationContext,\
                      coin: discord.Option(str),\
                      option: discord.Option(str),\
                      amount: discord.Option(str)):\
        await ctx.respond(f'\{amount\} \{coin\} has been \{option\}')\
\
    run(bot)\
\
\
if __name__ == '__main__':\
    main()\
}