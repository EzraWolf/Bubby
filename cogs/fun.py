
import random
import discord
import datetime
from typing import Optional
from Crypto.Hash import BLAKE2b
from discord.ext import commands

from assets import emojis


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='8ball',
        aliases=[
            '8b',
            '8-ball',
            '8balls',
        ],
        brief='Ask the magic 8-ball a question',
        usage='<text>',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
    )
    async def eight_ball(
        self,
        ctx: commands.Context, *, text: Optional[str] = None
    ):
        await ctx.reply(text)

    # ================================================================

    @commands.command(
        name='say',
        aliases=[
            'echo',
            'reply',
            'repeat',
            'repite',
        ],
        brief='Repeats what you have to say',
        usage='<text>',
        hidden=False,
        enabled=True,
        admin_only=False,
    )
    @commands.bot_has_permissions(
        send_messages=True,
        manage_messages=True
    )
    async def say(
        self,
        ctx: commands.Context,
        *, text: Optional[str] = None
    ):
        if text:
            if text == 'saul':
                await ctx.send(emojis.SAUL_GOODMAN)
                await ctx.message.delete()

            elif text == 'peter':
                await ctx.send(emojis.PETER_GRIFFIN)
                await ctx.message.delete()

            else:
                await ctx.send(text)
                await ctx.message.delete()

        else:
            await ctx.reply(
                f'You gotta say something {emojis.PEPE_1}',
                delete_after=5)
            await ctx.message.delete(delay=5)

    @commands.command(
        name='howbig',
        aliases=[
            'size',
            'hb',
            'pp',
            'penis',
        ],
        brief='How big is it!?',
        usage='None | <user>',
        hidden=False,
        enabled=True,
        admin_only=False,
        pass_context=True,
    )
    @commands.bot_has_permissions(
        send_messages=True,
    )
    async def howbig(
        self,
        ctx: commands.Context,
        member: Optional[discord.Member] = None
    ):
        hash = BLAKE2b.new(digest_bits=256)

        # EsmBot has a 0" bazingus with this seed
        # Do not change this because of that
        hash.update(b'lalalala')

        if member:
            hash.update(member.id.to_bytes(8, 'big'))
            random.seed(int(hash.hexdigest(), 16))
            size: int = random.randint(0, 20)
            embed = discord.Embed(
                title='Howbig detector',
                color=0x47FFA0 if size >= 12 else 0xFF4873,
                description=f'\
                    {member.display_name} you\'re about\
                    {round(size / 2.54, 1)}"\n\n\
                    8{"=" * size}D',
                timestamp=datetime.datetime.utcnow(),
            )

        else:
            hash.update(ctx.author.id.to_bytes(8, 'big'))
            random.seed(int(hash.hexdigest(), 16))
            size: int = random.randint(0, 20)
            embed = discord.Embed(
                title='Howbig detector',
                color=0x47FFA0 if size >= 12 else 0xFF4873,
                description=f'\
                    You\'re about {round(size / 2.54, 1)}"\n\n\
                    8{"=" * size}D',
                timestamp=datetime.datetime.utcnow(),
            )

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
