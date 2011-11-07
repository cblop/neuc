from scipy.io import loadmat
import numpy as np
import sys
from perceptron import *
import matplotlib.pyplot as plt

def loadData(mat_file):
    mat = loadmat(mat_file + '.mat', matlab_compatible=True)
    data = np.array(mat[mat_file])
    return data

def main():
    if (len(sys.argv) > 1):
        data = loadData(sys.argv[1])
        perc = Perceptron(data[0:2], data[2], 0.1)
        [loop, w] = perc.train(1000)
        print(w)
        w1 = np.sign(w) > 0
        w2 = np.sign(w) < 0
        print np.sign(w) - data[2]
        class1 = data[0:2, w1]
        class2 = data[0:2, w2]

        #class2[0,1] = data[w2]
        plt.scatter(class1[0], class1[1], c='r', marker='s')
        plt.scatter(class2[0], class2[1], c='b', marker='o')
        xaxis = np.array([-1,1])
        plt.plot(xaxis,  perc.weights.mean() * xaxis + 1)
        plt.show()

    else:
        print "Please enter the matlab file to load."

if __name__ == '__main__':
        status = main()

