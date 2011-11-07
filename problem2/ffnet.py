from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

def loadData(mat_file):
    mat = loadmat(mat_file + '.mat', matlab_compatible=True)
    data = np.array(mat[mat_file])
    return data

def main():
    if (len(sys.argv) > 1):
        data = loadData(sys.argv[1])
        inLayer = LinearLayer(2)
    else:
        print "Please enter the matlab file to load."


if __name__ == '__main__':
    status = main()




