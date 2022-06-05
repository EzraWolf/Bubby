
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='piglatin',
        aliases=[
            'pig',
            'piglatinize',
            'latin',
        ],
        brief='Converts text into pig latin',
        usage='<text>',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
        manage_messages=True,
    )
    async def piglatin(self, ctx: commands.Context):
        await ctx.send('WIP')


def setup(bot: commands.Bot):
    bot.add_cog(Utility(bot))
