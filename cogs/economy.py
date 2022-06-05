
from discord.ext import commands


class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='coinflip',
        aliases=[
            'flipcoin',
            'flip',
            'coin',
        ],
        brief='Make a decision or money with a coin flip',
        usage='None | <heads or tails> | <money amnt>',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
        manage_messages=True,
    )
    async def coinflip(self, ctx: commands.Context):
        await ctx.send('WIP')


def setup(bot: commands.Bot):
    bot.add_cog(Economy(bot))
