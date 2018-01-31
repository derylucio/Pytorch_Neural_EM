from torch.optim import Adam, SGD, RMSprop  
from sacred import Experiment
from dataprovider import make_data_iterator
from nem_model import NEM_model  
ex = Experiment("Pytorch-NEM")

@ex.config
def cfg():
	training = {
		'optimizer': 'adam', 
		'params' : {
			'learning_rate' : 1e-3,
		}
		'epochs' : 10, 
		'train_loc':"",
		'batch_size': 32
	}
	model_config = {

	}

@ex.capture 
def get_optimizer(model):
	lr = training['parameters']['learning_rate']
	optim_choice = training['optimizer']
	if optim_choice  == 'adam':
		return Adam(model.parameters(), lr=lr)
	elif optim_choice == 'rmsprop':
		return RMSprop(model.parameters(), lr=lr)
	else 
		return SGD(model.parameters(), lr=lr)


@ex.capture 
def run_epoch(model, optimizer):
	iterator = make_data_iterator('train', train_loc, training['batch_size'])
	for batch in iterator:
		# do naive structure for now
		optimizer.zero_grad()
		output = model(batch)
		gammas = model.E_step(output)
		mode.M_step(output, gammas, optimizer)
		



@ex.automain
def main():
	model = NEM_model(model_config)
	optimizer = get_optimizer(model)
	for i in range(training['epochs']):
		run_epoch(model, optimizer)


