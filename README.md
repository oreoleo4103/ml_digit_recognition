# ml_digit_recognition
This is a handwritten digit and mathematical operator recognition neural network, currently trained on the MNIST dataset from https://www.kaggle.com/datasets/michelheusser/handwritten-digits-and-operators.
The framework used for training is TensorFlow in python, which I chose for the sake of learning the framework. The sequential model accepts 28x28 black or white images, with two 16-neuron hidden layers and one 16-neuron output layer.
It is currently trained with roughly 200,000 data points and took roughly 15 minutes to train. All in all this lead to a 84% accuracy, but manual testing on different writing styles showed much less accuracy since the training dataset is not very good.
