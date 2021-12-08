import numpy as np # library for working with exponent
def sigmoid(x): # sigmoid function that multiplies inputs and weights
    return 1/ (1+np.exp(-x))
print(sigmoid(np.dot(np.array([0,0,1]), np.array([10,0,-5])))) # multipling inputs and weights