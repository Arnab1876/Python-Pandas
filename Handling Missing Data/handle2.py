#fillna()
# fillna(value, inplace=True)

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

#df.fillna(0,inplace=True)
#print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print('\nDataFrame after filling missing values:')
print(df)