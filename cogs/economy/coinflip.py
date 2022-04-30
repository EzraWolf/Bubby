
import random
from discord.ext import commands

class Coinflip(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name="coinflip",
		aliases=[
			'coin', 
			'flip',
		],
		brief='Make a coin flip, but give your bet before',
		enabled=True,
		hidden=False,
	)

	async def coinflip(self, message):
		await message.channel.send(f"{message.author.mention} flipped a coin and got {random.choice(['heads', 'tails'])}")

# Setup the cog
def setup(bot):
	bot.add_cog(Coinflip(bot))
