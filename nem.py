import torch.nn as nn
import torch.nn.Functional as F
from sacred import experiment

class NEM_model(nn.module):
	def __init__(self, latent_dim):
		super(NEM_model, self).__init__()

	def forward(self, data_batch):

	def E_step(self, out):
		# compute the gammas 

	def M_step(self, output, gammas, optim):
		loss.backward()
		optim.step()
