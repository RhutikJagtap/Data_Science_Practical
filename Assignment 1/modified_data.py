'''Set A-6).Write a Python program to drop ‘remarks’ column from the dataframe.
Also drop all null and empty values. Print the modified data.'''


# Display the data
df.loc[2] = [None, None, None]
df.loc[3] = ['Rhutik', '19', 69]
df.loc[4] = ['Sakshi', '18', 76]
df.loc[5] = [None, None, None]
df.loc[6] = ['Empty', '21', None]
df["remarks"] = None
Print(df.isnull())
