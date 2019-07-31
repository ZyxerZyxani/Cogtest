from redbot.core import commands
import sys
import discord
import asyncio
import platform
import random

class Mycog(commands.Cog):

    players = []
    @commands.command()
    async def team(self, ctx, *, x):
        players = [y.strip() for y in x.split(' ')]
        random.shuffle(players)
        y = len(players)/2
        msg = "Team 1:\n{}\n\nTeam 2:\n{}".format(players[:int(y)], players[int(y):])
        await ctx.send(msg)
