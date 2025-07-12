import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie","John","Mark","Stokes"],
    "Age": [25, 30, 35, 28, 40, 22],
    "City": ["Haryana", "Delhi", "Maharashtra", "Jharkhand", "U.P.", "Bihar"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000],
    "Performance": [85, 90, 95, 80, 75, 88]
}
df= pd.DataFrame(data)

#Displaying the dataframe----

print("Sample DataFrame----")
print(df)
print("Names (Single column return series)")
name=df['Name']
print(name)

#Selecting Multiple Columns----
subset=df[["Name", "Salary"]]
print('\nSubset with Name and Salary----')
print(subset) 