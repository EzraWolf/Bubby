
import random
import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if isinstance(message.channel, discord.channel.DMChannel):
            return

        if message.author.bot:
            return

        if random.randint(1, 50) == 1:
            await message.add_reaction('<:modular_peter_1:891151900332929085>')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return

        raise error


# Setup the Events cog
def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
