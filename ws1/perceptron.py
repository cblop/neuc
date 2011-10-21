import numpy as np

class Perceptron:
    def __init__(self, x, d, lr):
        self.inputs = np.vstack([x, np.ones((1,x.shape[1]))])
        self.desired = d
        #self.weights = np.zeros(x.shape)
        self.weights = np.random.random((self.inputs.shape[1], 1))
        self.lrate = lr

    def train(self, max_it):
        x = self.inputs
        w = self.weights
        d = self.desired
        y = np.zeros(d.shape)
        error = np.ones(d.shape)

        for i in xrange(max_it):
            y = np.sign(w.T * x)
            error = d - y
            for j in xrange(x.shape[0]):
                w = w + (self.lrate * error[j,:] * x[j,:])
            if error.sum() == 0:
                break
        
        self.weights = w

        return i, y


