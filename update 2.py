import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie","John","Mark","Stokes"],
    "Age": [25, 30, 35, 28, 40, 22],
    "City": ["Haryana", "Delhi", "Maharashtra", "Jharkhand", "U.P.", "Bihar"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000],
    "Performance": [85, 90, 95, 80, 75, 88]
}
df= pd.DataFrame(data)
print(df)

#Increasing salary by 5%

df['Salary'] = df['Salary'] * 1.05
print('\nDataFrame after increasing Salary by 5%:')
print(df)
