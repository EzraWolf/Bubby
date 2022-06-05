
from discord.ext import commands


class Example(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot: commands.Bot = bot

	# TODO: Add the command
	@commands.command(
		name='sha256',
		brief='Hashes text using SHA256',
		enabled=True,
		hidden=False,
	)
	async def sha256(self, message):
		await message.channel.send('TODO')
	
	# TODO: Add the command
	@commands.command(
		name='sha512',
		brief='Hashes text using SHA512',
		enabled=True,
		hidden=False,
	)
	async def sha512(self, message):
		await message.channel.send('TODO')
	
	# TODO: Add the command
	@commands.command(
		name='md5',
		brief='Hashes text using MD5 *UNSAFE*',
		enabled=True,
		hidden=False,
	)
	async def md5(self, message):
		await message.channel.send('TODO')
	
	# TODO: Add the command
	@commands.command(
		name='aes256',
		aliases=[
			'aes', 
		],
		brief='Encrypts / Decrypts a large message using AES256',
		enabled=True,
		hidden=False,
	)
	async def aes256(self, message):
		await message.channel.send('TODO')

	
	# TODO: Add the command
	@commands.command(
		name='fernet',
		brief='Encrypts / Decrypts a large message using Fernet',
		enabled=True,
		hidden=False,
	)
	async def fernet(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='secp256k1',
		brief='Encrypts / Decrypts information using SECP256K1',
		enabled=True,
		hidden=False,
	)
	async def secp256k1(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='rsa2048',
		brief='Encrypts / Decrypts information using RSA2048',
		enabled=True,
		hidden=False,
	)
	async def rsa2048(self, message):
		await message.channel.send('TODO')

	# TODO: Add the command
	@commands.command(
		name='hybrid',
		brief='Encrypts / Decrypts information using hybrid encryption (Fernet + SECP256K1)',
		enabled=True,
		hidden=False,
	)
	async def hybrid(self, message):
		await message.channel.send('TODO')

	
	# TODO: Add the command
	@commands.command(
		name='rot13',
		aliases=[
			'rot',
			'rotate',
			'rotate13',
		],
		brief='"Encrypts" or "Decrypts" text using ROT13, or provided amount of rotations',
		enabled=True,
		hidden=False,
	)
	async def rot13(self, message):
		await message.channel.send('TODO')

# Setup the cog
def setup(bot):
	bot.add_cog(Example(bot))
