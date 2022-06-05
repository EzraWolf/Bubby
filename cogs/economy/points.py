
# buy points for your server to unlock
# the ability to get more items and stuff

from typing import Optional
from discord.ext import commands


@commands.command(
    name='points',
    aliases=[
        'point',
        'experience',
        'exp',
        'xp',
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
async def points(
    ctx: commands.Context,
    *, text: Optional[str]
):
    await ctx.reply('WIP')


def setup(bot: commands.Bot):
    bot.add_command(points)
