
from typing import Optional
from discord.ext import commands


@commands.command(
    name='coinflip',
    aliases=[
        'coin',
        'flip',
        'flipcoin',
    ],
    brief='Flip a coin to make a decision or money',
    usage='<heads or tails> | <money amnt> | None',
    hidden=False,
    enabled=True,
    admin_only=False,
)
@commands.bot_has_permissions(
    send_messages=True,
)
async def coinflip(
    ctx: commands.Context,
    *, text: Optional[str]
):
    await ctx.reply('WIP')


def setup(bot: commands.Bot):
    bot.add_command(coinflip)
