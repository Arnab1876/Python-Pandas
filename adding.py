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

# square brackets df["Column_Name"] = some_Data

df["Bonus"]= df["Salary"] * 0.1
print('\nDataFrame after adding Bonus column:')
print(df)

# Using insert()
#df.insert(loc,"Column_Name", some_data)

df.insert(0, "Employee ID", [101,102,103,104,105,106])
print('\nDataFrame after inserting Employee ID column at index 0:')
print(df)