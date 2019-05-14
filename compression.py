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

if __name__ == '__main__':
    print("ipython compression.py image reduzedDimension"+ "\n"+ 
          "- reduzedDimension: Dimension reduzed to reduction")
    file = sys.argv[1]
    k = int(sys.argv[2])
    # Reading image
    img = mpimg.imread(file)
    m = img.shape[0] 
    n = img.shape[1]
    
    # Singular Value Decomposition
    U, S, V = linalg.svd( img[:, :, 0] )
    print( "Dimensao de U, S, V, respectivamente" )
    print( U.shape, S.shape, V.shape )

    # Reconstruct SVD
    #Sigma = np.zeros((m, n))
    #Sigma[:n, :n] = np.diag(S)
    
    #imgReconstruct = np.dot( np.dot( U, Sigma ), V )
    #imgplot = plt.imshow( imgReconstruct )


    # Reduzed SVD
    reduzedU = U[:, :k]
    reduzedV = V[:k, :]
    reduzedS = np.zeros((k, k))
    reduzedS[:k, :k] = np.diag(S[:k])
    print( "Dimensao de U, S, V, respectivamente, apos a reducao" )
    print( reduzedU.shape, reduzedS.shape, reduzedV.shape )

    imgReduzed = np.dot( np.dot( reduzedU, reduzedS ), reduzedV )
    imgplot = plt.imshow( imgReduzed )
    
    plt.show()
    
