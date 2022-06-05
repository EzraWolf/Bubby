
from discord.ext import commands


class Memes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        name='meme',
        aliases=[
            'memes',
            'dankmeme',
            'dankmemes',
        ],
        brief='I\'ll send you a random meme from r/dankmemes',
        usage='None',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
    )
    async def meme(self, ctx: commands.Context):
        await ctx.send('WIP')


def setup(bot: commands.Bot):
    bot.add_cog(Memes(bot))
