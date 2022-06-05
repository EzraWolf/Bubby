
import discord
import datetime
from discord.ext import commands

from assets import emojis


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='ping',
        aliases=[
            'p',
            'latency',
            'lat',
            'lag',
        ],
        brief='Returns the bots latency',
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
    async def ping(self, ctx: commands.Context):
        embed = discord.Embed(
            title='Pong ' + emojis.PEPE_1,
            color=0x47FFB8,
            description=f'{round(self.bot.latency * 1000, 3)}ms',
            timestamp=datetime.datetime.utcnow(),
        )
        await ctx.send(embed=embed)


class NewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        dest = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(
                color=0x47CAFE,
                description=page,
                timestamp=datetime.datetime.utcnow(),
            )
            await dest.send(embed=embed)

    async def send_command_help(self, command):
        self.add_command_formatting(command)
        self.paginator.close_page()
        await self.send_pages()


def setup(bot: commands.Bot):
    bot.help_command = NewHelp()
    bot.add_cog(General(bot))
