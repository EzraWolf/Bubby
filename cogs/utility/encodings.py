
from discord.ext import commands

class Encodings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# TODO: Add the command
	@commands.command(
		name='morse',
		aliases=[
			'morsecode',
		],
		brief='Encodes or decodes morse code',
		enabled=True,
		hidden=False,
	)
	async def encode(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='galactic',
		aliases=[
			'enchant',
			'enchantment',
			'gal',
		],
		brief='Encodes or decodes galactic alphabet (MC enchantment table)',
		enabled=True,
		hidden=False,
	)
	async def galactic(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='base64',
		aliases=[
			'b64',
		],
		brief='Encodes or decodes base64',
		enabled=True,
		hidden=False,
	)
	async def base64(self, message):
		await message.channel.send('TODO')
	
	# TODO: Add the command
	@commands.command(
		name='base32',
		aliases=[
			'b32', 
		],
		brief='Encodes or decodes base32',
		enabled=True,
		hidden=False,
	)
	async def base32(self, message):
		await message.channel.send('TODO')

# Setup the cog
def setup(bot):
	bot.add_cog(Encodings(bot))
