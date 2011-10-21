import numpy as np

class Perceptron:
    def __init__(self, x, d, b, lr):
        self.inputs = x
        self.desired = d
        #self.weights = np.zeros(x.shape)
        self.weights = np.random.random((x.shape[0], x.shape[1]))
        self.bias = b
        self.lrate = lr

    def train(self, max_it):
        x = self.inputs
        w = self.weights
        b = self.bias
        d = self.desired
        y = np.zeros(d.shape)
        error = np.ones(x.shape)

        for i in xrange(max_it):
            y = np.sign(w * x + b)
            error = d - y
            w = w + (self.lrate * error * x)
            b = b + self.lrate * error
            if error.sum() == 0:
                break
            
        return i, y


