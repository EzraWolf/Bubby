
import keras
import numpy as np

class NeuralNet(object):
	def __init__(
		self,
		inp_ct      : int,
		hid_ct      : int,
		hid_layer_ct: int,
		out_ct      : int,
		weights     : list[float]=None,
		model	    : keras.Model=None,
	):
		self.inp_ct : int         = inp_ct
		self.hid_ct : int         = hid_ct
		self.out_ct : int         = out_ct
		self.weights: list[float] = weights
		self.model  : keras.Model = model


class LSTM(object):
	def __init__(self, inp_ct, hid_ct, hid_layer_ct, out_ct):

		self.inp_ct       = inp_ct
		self.hid_ct       = hid_ct
		self.hid_layer_ct = hid_layer_ct
		self.out_ct       = out_ct

		self.model = keras.models.Sequential()

	def create_model(self) -> NeuralNet:
		
		# Store values in the object to act as a
		# temporary storage for the model, which
		# will periodically be updated and saved
		# to their respective text files.
		net = NeuralNet(self.inp_ct, self.hid_ct, self.hid_layer_ct, self.out_ct)

		# Create the model
		self.model.add(
			keras.layers.recurrent.LSTM(
				self.hid_ct,
				input_shape=(None, self.inp_ct),
				return_sequences=True
			)
		)

		# Add the hidden layers
		for _ in range(self.hid_layer_ct - 1):
			self.model.add(keras.layers.recurrent.LSTM(self.hid_ct, return_sequences=True))
		
		self.model.add(keras.layers.core.Activation('softmax'))
		self.model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

		res = []
		for i in range(100):
			a = self.model.predict('huh ?')
			res.append(a)
		
		print(res)

		net.model = self.model
		return res