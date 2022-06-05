
# TODO:
# - Implement a simulated economy
# - the more people buy the more inflation gets
# - over time the less people buy inflation goes down
# - place tarrifs on other users or servers
# - place stocks on users or servers
# - 1 stock = 50k coins or something
# - 1 stock = +0.5% inflation
# - users or servers have a set value for their stocks
#   based off of how much they make on idle

from typing import Optional
from discord.ext import commands


@commands.command(
    name='economy',
    aliases=[
        'econ',
    ],
    brief='WIP',
    usage='None',
    hidden=False,
    enabled=False,
    admin_only=False,
)
@commands.bot_has_permissions(
    send_messages=True,
)
async def economy(
    ctx: commands.Context,
    *, text: Optional[str]
):
    await ctx.reply('WIP')


def setup(bot: commands.Bot):
    bot.add_command(economy)
