
from discord.ext import commands


class Images(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='magic',
        aliases=[
            'magik',
            'warp',
        ],
        brief='Warps an image in a funny way',
        usage='None | <intensity>',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
        manage_messages=True,
    )
    async def magic(self, ctx: commands.Context):
        await ctx.send('WIP')


def setup(bot: commands.Bot):
    bot.add_cog(Images(bot))
