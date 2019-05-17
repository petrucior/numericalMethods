#!/usr/bin/python
#coding: utf-8

# file: compression.py
# brief: This file contains a simple compression image using SVD decomposition
# author: Petrucio Ricardo Tavares de Medeiros
# date: 13/05/2019

import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import linalg
import numpy as np

# RBG to Grayscale function
def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

if __name__ == '__main__':
    print("ipython compression.py image reduzedDimension"+ "\n"+ 
          "- reduzedDimension: Dimension reduzed to reduction")
    file = sys.argv[1]
    k = int(sys.argv[2])
    # Reading image
    img = mpimg.imread(file)
    # Converting RGB to Grayscale
    img = rgb2gray( img )
    print(img.shape)
    m = img.shape[0] 
    n = img.shape[1]
    
    # Singular Value Decomposition
    U, S, V = linalg.svd( img[:, :] )
    print( "Dimensao de U, S, V, respectivamente" )
    print( U.shape, S.shape, V.shape )

    # Reconstruct SVD
    #Sigma = np.zeros((m, n))
    #Sigma[:n, :n] = np.diag(S)
    
    #imgReconstruct = np.dot( np.dot( U, Sigma ), V )
    #imgplot = plt.imshow( imgReconstruct, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)


    # Reduzed SVD
    reduzedU = U[:, :k]
    reduzedV = V[:k, :]
    reduzedS = np.zeros((k, k))
    reduzedS[:k, :k] = np.diag(S[:k])
    print( "Dimensao de U, S, V, respectivamente, apos a reducao" )
    print( reduzedU.shape, reduzedS.shape, reduzedV.shape )

    imgReduzed = np.dot( np.dot( reduzedU, reduzedS ), reduzedV )
    imgplot = plt.imshow( imgReduzed, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    
    
    plt.show()
    
