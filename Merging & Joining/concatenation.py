"""
vertically--(row-wise)
horizontally--(column-wise)
pd.concate([df1, df2] , axis= 0 or 1, ignore_index=True)
[df1,df2] = List of DataFrames to concatenate.
By setting axis = 1 : It concatenates Horizontally.
By default or with axis= 0 : It concatenates Vertically.
ignore_index =True : It resets the index of the concatenated DataFrame.

"""

import pandas as pd

#Region1:-

df_region1=pd.DataFrame({
"CustomerID": [1,2],
"Name":  ['Gopal','Raju']
})

#Region2:-

df_region2=pd.DataFrame({
    "CustomerID": [3,4],
    "Name":  ['Shyam','Mohit']
})

# Concatenating vertically::--

df_concat=pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print("Concatenated DataFrame vertically:")
print(df_concat)