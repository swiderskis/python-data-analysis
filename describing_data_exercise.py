"""
The first function reads the file "auto-mpg.data", defines its headers, 
accounts for whitespace, and returns it.
The second function finds the mean of the agg_var variable for each group_var
group, and returns it.
The data file used can be obtained from
https://archive.ics.uci.edu/ml/datasets/Auto+MPG.
This is an exercise for the "Python Data Analysis and Visualisation" course on
Educative.
"""

import pandas as pd
def read_csv():
    
    #Headers of columns in file "auto-mpg.data"
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", 
             "acceleration", "model_year", "origin", "car_name"]
    df = pd.read_csv("auto-mpg.data", header = None, names = names, 
                     delim_whitespace = True)
    
    return df

def group_aggregation(df, group_var, agg_var):
    
    df_mean = df.groupby(group_var)[agg_var].mean()
    
    return df_mean
