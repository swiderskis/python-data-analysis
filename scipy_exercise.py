"""
This function takes two numpy arrays as an input and returns their correlation and p-value.
This is an exercise for the "Python Data Analysis and Visualisation" course on Educative.
"""

from scipy import stats
import numpy as np

def correlation(array1, array2):

  correlation = stats.pearsonr(array1, array2)[0]
  pvalue = stats.pearsonr(array1, array2)[1]

  return (correlation, pvalue)