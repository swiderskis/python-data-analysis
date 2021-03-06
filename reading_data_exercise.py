"""
This function reads the file "auto-mpg.data", defines its headers, accounts
for whitespace, and returns its shape.
The data file used can be obtained from
https://archive.ics.uci.edu/ml/datasets/Auto+MPG.
This is an exercise for the "Python Data Analysis and Visualisation" course on
Educative.
"""

import pandas as pd

def read_csv():

    #Headers of columns in file "auto-mpg.data"
    names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
             'acceleration', 'model_year', 'origin', 'car_name']
   
    df = pd.read_csv("auto-mpg.data", header = None, names = names, 
                     delim_whitespace = True)

    return df.shape
