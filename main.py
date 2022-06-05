
import discord
from discord.ext import commands
from rich.console import Console

import config


class Bubby(commands.Bot):
    def __init__(self):
        """
        Initialize the bot under commands.Bot,
        this is the main class for Bubby  bot.
        """

        self.was_ready = False

        # Figure out our intents
        if config.ALL_INTENTS:
            intents = discord.Intents.all()
        else:
            intents = discord.Intents.default()

        super().__init__(
            command_prefix=commands.when_mentioned_or(config.PREFIX),
            intents=intents,
            strip_after_prefix=True,
            case_insensitive=True,
            shard_count=config.SHARD_CT
        )

    async def on_ready(self):
        r = Console()
        r.log(f'Logged in as {self.user.name}')

        # Ensure that the bot has only been initialized once
        if not self.was_ready:
            self.was_ready = True
            await self.init()

    async def init(self):

        # Load the cogs & single command files with no cog class
        for cog in config.COG_PATHS:
            self.load_extension(cog)

            # TODO: Make a more pretty logging system
            print(f"Loaded {cog}")
        print('Successfully loaded all cogs')


if __name__ == '__main__':
    bot = Bubby()
    bot.run(config.TOKEN)
