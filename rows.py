#head(), tail() 
#head(n) --returns the first n rows of the DataFrame
#tail(n) --returns the last n rows of the DataFrame
#By default it return 5 rows if no range given..

import pandas as pd
df= pd.read_json("sample_Data.json")
print("Display first 10 rows of the DataFrame:")
print(df.head(10))

print("Display last 10 rows of the DataFrame:")
print(df.tail(10))
