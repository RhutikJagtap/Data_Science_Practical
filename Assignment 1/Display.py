'''Set A -4).Write a Python program to Add 5 rows with duplicate values and missing values.
Add a column ‘remarks’ with empty values.'''


# Display the data
df.loc[2] = [None, None, None]
df.loc[3] = ['Rhutik', '19', 69]
df.loc[4] = ['Sakshi', '18', 76]
df.loc[5] = [None, None, None]
df.loc[6] = ['Empty', '21', None]
df["remarks"] = None
Print(df)
