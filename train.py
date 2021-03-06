"""This script provides an environment and hyper parameters to trains the
neuron network.
"""


import mnist_loader as loader
import network


# import data set
path = './mnist.pkl.gz'
train_data, validation_data, test_data = loader.load_data_wrapper(path)

# hyper parameters
# create a neuron network with a sizes list specifying the number of neurons
# in each layer
net = network.Network([784, 30, 10])
mini_batch_size = 10
epochs = 30
eta = 3.0

# train and test
net.sgd(train_data, mini_batch_size, epochs, eta, test_data)
