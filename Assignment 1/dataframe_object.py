# set B-2).Write a Python program to find the shape, size, datatypes of the dataframe object.

import pandas as pd
df = pd.read_csv("SOCR-HeightWeight.csv")
print("Shape of the data:")
print(df.shape)
print("\n\nData Type:")
print(df.dtypes)
print("\n\nHead data:")
print(df.head())
