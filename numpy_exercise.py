"""
This function takes a numpy array as an input and returns the max, std, sum, and dot product.
This is an exercise for the "Python Data Analysis and Visualisation" course on Educative.
"""

import numpy as np

def perform_calculations(array):
  
  arraymax = np.max(array)
  arraystd = np.std(array)
  arraysum = np.sum(array)
  arraydot = np.dot(array,array)

  return arraymax, arraystd, arraysum, arraydot