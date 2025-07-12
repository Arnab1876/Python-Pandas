# dropna()
#df.dropna(axis=0, inplace=True)  # Drop rows with any NaN values
#df.dropna(axis=1, inplace=True)  # Drop columns with any NaN values

import pandas as pd

data={
    "Name": ["Alice", None, "Charlie","John","Mark","Stokes"],
    "Age": [25, None, 35, 28, 40, 22],
    "City": ["Haryana", None, "Maharashtra", "Jharkhand", "U.P.", "Bihar"],
    "Salary": [50000, None, 70000, 80000, 90000, 100000],
    "Performance": [85, None, 95, 80, 75, 88]
}
df= pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)