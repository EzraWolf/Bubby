
# TODO:
# - Implement this command to buy upgrades for
#   the server and the user.
# - Add a command to list the upgrades
# - Make it so you can buy upgrades for less tax on the user
# - Make it so you can buy upgrades for less tax on the server
# - Make it so you can get discounts on upgrades
# - Make it so you can get 1.1x, 1.2, etc on all money you get
# - Reduce cooldown on things
# - Place larger tarrifs on other users or servers

from typing import Optional
from discord.ext import commands


@commands.command(
    name='upgrades',
    aliases=[
        'upgrade',
        'updates',
        'update',
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
async def upgrades(
    ctx: commands.Context,
    *, text: Optional[str]
):
    await ctx.reply('WIP')


def setup(bot: commands.Bot):
    bot.add_command(upgrades)
