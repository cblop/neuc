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
        perc = Perceptron(data[0:2], data[2], 1, 0.1)
        w = perc.train(10)
        #data[2]
        w1 = w[1][0] > 0
        w2 = w[1][0] < 0
        class1 = data[0:2, w1]
        class2 = data[0:2, w2]

        #class2[0,1] = data[w2]
        plt.scatter(class1[0], class1[1], c='r', marker='s')
        plt.scatter(class2[0], class2[1], c='b', marker='o')
        plt.show()

    else:
        print "Please enter the matlab file to load."

if __name__ == '__main__':
        status = main()

