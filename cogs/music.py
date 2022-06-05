
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='play',
        aliases=[
            'playsong',
        ],
        brief='Play a song in VC',
        usage='<spotify link> | <youtube link> | \
            <soundcloud link> | <.mp3 or .wav>',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
        manage_messages=True,
    )
    async def play(self, ctx: commands.Context):
        await ctx.send('WIP')


def setup(bot: commands.Bot):
    bot.add_cog(Music(bot))
