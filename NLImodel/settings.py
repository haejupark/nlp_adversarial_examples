import sys

class Setting(object):
	def __init__(self):
		self.lr = 0.01
		self.word_dim = 300
		self.lstm_dim = 256
		self.max_len = 30
		self.dense_dim =  128
		self.keep_prob = 0.6
		self.batch_size = 1024
		self.epochs = 50
    # your directory here
		self.train_dir = "data/xnli-mt/multinli/"
		self.dev_dir = "data/xnli/"
		self.embed_dir = "../aaai2019/data/"

labels = {'neutral':0, 'entailment':1, 'contradiction':2}
labels_reverse = {0:'neutral', 1:'entailment', 2:'contradiction'}
