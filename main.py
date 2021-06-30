import numpy as np
from math import exp
from random import random
from pprint import pprint

class Network:
	
	def __init__(self, annMap):
		self.sigma 			= np.vectorize(lambda x : 1 / (1 + exp(-x)))
		self.sigmaPrime 	= np.vectorize(lambda x : exp(-x) / (1 + 2 * exp(-x) + exp(-2 * x)))
		self.reLU 			= np.vectorize(lambda x : max(0, x))
		self.reLUPrime		= np.vectorize(lambda x : max(0, x / abs(x)))
		self.costFunction	= lambda x,y : np.sum((x - y) ** 2)

		self.layers = []
		self.bias = [np.random.rand(e) for e in annMap[1:]]
		print(self.bias)
		for i in range(1,len(annMap)):
			self.layers.append(self.newLayer(annMap[i-1], annMap[i]))

	def train(self, inputs, iter):
		for i in range(iter):
			cost = 0
			for j in inputs:
				result = self.run(j[0])
				cost += self.costFunction(result, j[1])
			cost /= len(inputs)
			print(cost)



	def run(self, inputs):
		neurons  = inputs
		for i in range(len(self.layers)):
			neurons = self.sigma(self.layers[i].dot(neurons)+self.bias[i])
		return neurons
		
	def backProp(self):
		pass
	
	def newLayer(self,a,b):
		return np.random.rand(b,a) * 2 - 1

mapping = (3,4,4,2)
inputData = (
	([0,0,0],[1,0]),
	([0,0,1],[0,1]),
	([0,1,0],[1,0]),
	([0,1,1],[0,1]),
	([1,0,0],[1,0]),
	([1,0,1],[0,1]),
	([1,1,0],[1,0]),
	([1,1,1],[0,1])
)

network = Network(mapping)
network.train(inputData,1)
result = network.run([0,1,1])
print(result)