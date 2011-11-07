from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from scipy.io import loadmat
import numpy as np
import sys
import matplotlib.pyplot as plt

def loadData(mat_file):
    mat = loadmat(mat_file + '.mat', matlab_compatible=True)
    #data = np.array(mat[mat_file])
    #data = np.array(mat)

    #print(data)
    return mat

def build_net(n_in, n_hidden, n_out):
    n = FeedForwardNetwork()

    inLayer = LinearLayer(n_in)
    hiddenLayer = SigmoidLayer(n_hidden)
    outLayer = LinearLayer(n_out)

    n.addInputModule(inLayer)
    n.addModule(hiddenLayer)
    n.addOutputModule(outLayer)

    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)

    n.addConnection(in_to_hidden)
    n.addConnection(hidden_to_out)

    n.sortModules()

    return n

def build_dataset(inputs, targets):
    ds = SupervisedDataSet(inputs.shape[0], targets.shape[0])
    [ds.appendLinket(x, y) for x in inputs for y in targets]
    #ds.appendLinked(inputs, targets)
    print ds
    return ds


def main():
    if (len(sys.argv) > 1):
        data = loadData(sys.argv[1])
        inputs = np.array(data['houseInputs'])
        targets = np.array(data['houseTargets'])

        ds = build_dataset(inputs, targets)

        n = build_net(inputs.shape[0], 20, 1)
        print n
    else:
        print "Please enter the matlab file to load."


if __name__ == '__main__':
    status = main()




