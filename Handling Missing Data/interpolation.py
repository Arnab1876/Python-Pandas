import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie","John","Mark","Stokes"],
    "Age": [25, None, 35, 28, 40, 22],
    "City": ["Haryana", "Delhi", "Maharashtra", "Jharkhand", "U.P.", "Bihar"],
    "Salary": [50000, None, 70000, 80000, 90000, 100000],
    "Performance": [85, None, 95, 80, 75, 88]
}
df= pd.DataFrame(data)
print(df)

# Linear,Polynomial,Time  --Interpolation diff. methods

df.interpolate(method="linear",axis=0,inplace=True)
print('\nDataFrame after linear interpolation:')
print(df)