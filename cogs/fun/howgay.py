
from discord.ext import commands


@commands.command(
    name='howgay',
    aliases=[
        'hg',
        'gay',
    ],
    brief='How gay are you!?',
    usage='None | <user>',
    hidden=False,
    enabled=True,
    admin_only=False,
)
@commands.bot_has_permissions(
    send_messages=True,
)
async def howgay(ctx: commands.Context, *, text: str):
    await ctx.reply(text)


def setup(bot: commands.Bot):
    bot.add_command(howgay)
