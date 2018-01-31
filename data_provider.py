import glob 
import numpy as np 
from PIL import Image 
import torch 
from torch.autograd import Variable

def make_data_iterator(data_loc, batch_size):
	images = glob.glob(os.path.join(data_loc, "*"))
	perm = np.random.permutation(len(images))
	num_batches = len(images) // batch_size
	for i in range(num_batches):
		batch_imgs = images[perm[i*(batch_size) : (i + 1)*batch_size]]
		batch_imgs = [torch.FloatTensor(Image.open(fname).unsqueeze(0)) for fname in batch_imgs]
		batch_imgs = torch.cat(batch_imgs)
		yield Variable(batch_imgs)



