
from discord.ext import commands


class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Add the command
    @commands.command(
        name='yomama',
        aliases=[
            'yo',
            'urmom',
        ],
        brief='Behold the worlds greatest jokes in one command',
        enabled=True,
        hidden=False,
    )
    async def Yomama(self, message):
        await message.channel.send('TODO')

    # TODO: Add the command
    @commands.command(
        name='dadjoke',
        aliases=[
            'dad',
            'dadjokes',
            'yodaddy',
            'yodad',
        ],
        brief='Behold the worlds second greatest jokes in one command',
        enabled=True,
        hidden=False,
    )
    async def Dadjoke(self, message):
        await message.channel.send('TODO')


# Setup the cog
def setup(bot: commands.Bot):
    bot.add_cog(Jokes(bot))
