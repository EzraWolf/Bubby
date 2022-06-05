
from typing import Optional
from discord.ext import commands

from assets import emojis
import config


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='reload',
        aliases=[
            'r',
            'restart',
            'reboot',
            'reset',
        ],
        brief='Reloads the cogs in the machine',
        usage='None | <cog name>',
        hidden=True,
        enabled=True,
        admin_only=True,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
        manage_messages=True,
    )
    @commands.is_owner()
    async def reload(
        self,
        ctx: commands.Context,
        *, text: Optional[str] = None
    ):

        # Load the cogs & single command files with no cog class
        for cog in config.COG_PATHS:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        print('Successfully reloaded all cogs')

        # Remove the command message
        await ctx.message.add_reaction(emojis.PEPE_2)


def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))
