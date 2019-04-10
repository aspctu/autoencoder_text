#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:30:14 2018

@author: abqader
"""

import cv2
from matplotlib import pyplot as plt

def plotHist(imagePath):
    '''
    imagePath: path to image 
    
    Displays plot of color histogram 
    '''
    histGram = saveHist(imagePath)
    
    plt.plot(histGram)
    plt.show()

    
def saveHist(imagePath):
    '''
    imagePath: path to image 
    
    Returns flattened vector of histogram
    '''
    img = cv2.imread(imagePath)
    histGram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    histGram = histGram.flatten()
    
    return(histGram)