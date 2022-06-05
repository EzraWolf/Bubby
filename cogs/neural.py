
# from neural.lstm import LSTM
from discord.ext import commands

# import config


class Neural(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='predict',
        aliases=[
            'nn',
            'neural',
            'neuralnet',
            'neuralnetwork',
            'lstm',
        ],
        brief='Make the neural network say something',
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
    async def predict(self, ctx: commands.Context):
        # lstm = LSTM(
        #     50,
        #     config.NN_HIDDEN_CELL_CT,
        #     config.NN_HIDDEN_LAYER_CT,
        #     50)
        # res = lstm.create_model()
        await ctx.send('WIP')


def setup(bot: commands.Bot):
    bot.add_cog(Neural(bot))
