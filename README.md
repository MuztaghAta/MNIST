# MNIST
This is a well-known toy project, I play it for studying the book 'Neural Networks and Deep Learning' by Michael Nielsen. 

The codes is written for Python 3.6. I wrote (not copy for the book) most of the codes by myself to see whether my own codes works, and more importantly I want to improve my coding skill by comparing my codes with the codes provided in the book. Besides, coding line by line really helps understand the theory of neural networks since you have to recall the theory many times when writing the codes. It's also worth mentioning that the modules that I wrote (e.g. network2.py and analysis.py) provide more features than the ones provided by the NNDL book.

All the basic and fundamental components of a neural network, like feedforward, backpropagation, stochastic gradient descent, relularization, and dropout, are implemented from scrach rather than calling the methods from Tensorflow or Keras, which would be much much handy but less less helpful to understand the theory and the algorithms.

# the 1st network class
network.py - neural network class, 
train.py - training environment, 
mnist_loader.py - data loader

I created a main script 'train.py' that loads the mnist data, specifies hyperparameters and trains the network. I also did some changes to the module of 'mnist_loader' so that data path can be specified in 'train.py'. 

# the 2nd network class
activation_cost.py - activation+cost classes, 
analysis2.py - plot performance results, 
mnist_loader.py - data loader, 
network2.py - the 2nd network class, 
train2.py - training enviroment, 
network2_keras.py, 
train2_keras.py, 
vanilla_model_classic.h5 

The modules for the 2nd network class include a number of features that are not supported by those for the 1st network class. 

The 2nd network class enables 1) matrix-based approach to back propagation, 2) network initialization with different activation+cost functions, 3) monitor runtime, prediction accuracy and cost, 4) L2 regularization and dropout (neurons of hidden layers), 5) different weights/biases initialization approaches, and 6) save and load trained network model. Note that some of the above features are not implemented in the codes for the NNDL book including 2, runtime monitoring in 3 and dropout in 4. 

The analysis2.py module defines a method that can plot any dimension of the training results, including runtime, accuracy and cost on training/evaluation data.

The above network was also implemented suing Keras, which takes significantly less codes. A trained model with good evaluation accuracy (~ 98%), namely, vanilla_model_classic.h5, was saved for prediction. 

# the 3rd network class
network3_keras.py - convolutional network model, 
train3_keras.py - trainning environment, 
processing.py - process pictures of handwritten digits, 
recognize.py - recognize handwritten digits in a picture, 
cnn_model_classic.h5 - trained model with good evaluation accuracy (~ 99%), 
IMG_1702.jpg, IMG_1703.jpg - examples for prediction, 
requirements.txt - packages/modules used in this project

The 3th network, convolutional network, is fully implemented using Keras. In addition, a module for recognizing any handwritten digits in picture is developped using opencv. Two examples are included, which can be correctly recognized by the saved cnn model. You can use the saved model to recognize digits in any other pictures, just change the 'path' in line 10 in recognize.py to the path of the picture you want to recognize.
