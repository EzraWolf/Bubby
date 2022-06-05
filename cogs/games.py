
from discord.ext import commands


class Games(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='blackjack',
        aliases=[
            'bj',
        ],
        brief='Play a game of blackjack',
        usage='None',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
        manage_messages=True,
    )
    async def blackjack(self, ctx: commands.Context):
        await ctx.send('WIP')


def setup(bot: commands.Bot):
    bot.add_cog(Games(bot))
