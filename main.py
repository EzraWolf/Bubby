
import os
import pathlib
import discord
from discord.ext import commands

import config

class Bubby(commands.Bot):
	def __init__(self) -> None:
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

		# TODO: Make a more pretty logging system
		print(f"Logged in as {self.user.name}")

		if not self.was_ready:
			self.was_ready = True
			await self.initialize()
			
	async def initialize(self):

		# Load the events
		self.load_extension('cogs.events')

		# Load the cogs
		for path in config.COG_PATHS:
			for file in pathlib.Path(path.replace('.', '/')).glob('*.py'):
				self.load_extension('{}.{}'.format(path, file.stem))

				# TODO: Make a more pretty logging system
				print(f"Loaded {file.stem}")
		
if __name__ == '__main__':

	# TODO: Change fixed location
	bot = Bubby()
	bot.run(config.TOKEN)
