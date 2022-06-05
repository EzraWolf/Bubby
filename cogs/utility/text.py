
from discord.ext import commands

class Text(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# TODO: Add the command
	@commands.command(
		name='fliptext',
		aliases=[
			'rev',
			'reverse',
			'fliptxt',
		],
		brief='Flips text from "Hello" to "olleH"',
		enabled=True,
		hidden=False,
	)
	async def fliptext(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='uppercase',
		aliases=[
			'cap',
			'capital',
			'capitalize',
			'upper',
			'ucase',
		],
		brief='Converts text to uppercase in various ways',
		enabled=True,
		hidden=False,
	)
	async def uppercase(self, message):
		await message.channel.send('TODO')
	
	# TODO: Add the command
	@commands.command(
		name="lowercase",
		aliases=[
			'lower',
			'lcase',
		],
		brief='Converts text to lowercase in various ways',
		enabled=True,
		hidden=False,
	)
	async def lowercase(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name="randletters",
		aliases=[
			'randomletters',
			'randomchars',
			'randchars',
		],
		brief='Generates pseudo-random ASCII characters',
		description='Generates a string of pseudo-random ASCII characters using\
			a provided string as a seed, or otherwise by using cryptographically\
			secure randomness through os.urandom()',
		enabled=True,
		hidden=False,
	)
	async def flip(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='piglatin',
		aliases=[
			'pigl',
			'pig',
			'latin',
			'pibbay',
			'pibbayspeak',
		],
		brief='Translates text into pig latin',
		enabled=True,
		hidden=False,
	)
	async def piglatin(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='cancer',
		aliases=[
			'owo',
			'uwu',
			'owoify',
			'uwuify',
		],
		brief='Makes the earth destroid',
		enabled=True,
		hidden=False,
	)
	async def cancer(self, message):
		await message.channel.send('TODO')

# Setup the cog
def setup(bot):
	bot.add_cog(Text(bot))
