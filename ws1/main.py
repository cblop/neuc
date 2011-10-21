from scipy.io import loadmat
import numpy as np
import sys

def loadData(mat_file):
    mat = loadmat(mat_file + '.mat', matlab_compatible=True)
    data = np.array(mat[mat_file])
    return data

def main():
    if (len(sys.argv) > 1):
        data = loadData(sys.argv[1])
        print(data)
    else:
        print "Please enter the matlab file to load."

if __name__ == '__main__':
        status = main()

